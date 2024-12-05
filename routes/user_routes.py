from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
#from app import db
from database import db
from models import User, BorrowRequest, Book
from datetime import datetime
from utils.csv_export import generate_csv  # type: ignore # Import your CSV utility function


user_bp = Blueprint('user_bp', __name__)

# Get list of books
@user_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    books_list = [{"id": book.id, "title": book.title, "author": book.author} for book in books]
    return jsonify(books_list)

# Submit a borrow request
@user_bp.route('/borrow_request', methods=['POST'])
def borrow_book():
    data = request.get_json()
    user_id = data.get('user_id')
    book_id = data.get('book_id')
    start_date = datetime.strptime(data.get('start_date'), '%Y-%m-%d')
    end_date = datetime.strptime(data.get('end_date'), '%Y-%m-%d')
    
    existing_request = BorrowRequest.query.filter_by(book_id=book_id, status='Approved').filter(
        BorrowRequest.start_date <= end_date, BorrowRequest.end_date >= start_date).first()
    
    if existing_request:
        return jsonify({"message": "Book is already borrowed during this period"}), 400
    
    new_request = BorrowRequest(user_id=user_id, book_id=book_id, start_date=start_date, end_date=end_date)
    db.session.add(new_request)
    db.session.commit()
    
    return jsonify({"message": "Borrow request submitted successfully"}), 201

@user_bp.route('/download_borrow_history', methods=['GET'])
@jwt_required()  # Protect the endpoint
def download_borrow_history():
    # Get the currently logged-in user's ID
    current_user_id = get_jwt_identity()
    
    # Fetch borrow history for the user
    borrow_requests = BorrowRequest.query.filter_by(user_id=current_user_id).all()
    
    # If no history found
    if not borrow_requests:
        return jsonify({"message": "No borrow history found."}), 404

    # Prepare the data for CSV
    csv_data = []
    for req in borrow_requests:
        csv_data.append({
            "Borrow Request ID": req.id,
            "Book ID": req.book_id,
            "Start Date": req.start_date.strftime('%Y-%m-%d'),
            "End Date": req.end_date.strftime('%Y-%m-%d'),
            "Status": req.status
        })

    # Generate CSV response
    return generate_csv(csv_data)
