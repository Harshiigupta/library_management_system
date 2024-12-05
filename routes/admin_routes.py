from flask import Blueprint, request, jsonify
#from app import db
from database import db 
from models import User, BorrowRequest, Book
from datetime import datetime

admin_bp = Blueprint('admin_bp', __name__)

# Create new user
@admin_bp.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')

    password = data.get('password')
    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "User already exists"}), 400
    
    # if User.query.filter_by(email=email).first():
    #     return jsonify({"message": "User already exists"}), 400
    
    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User created successfully"}), 201

# View all borrow requests
@admin_bp.route('/borrow_requests', methods=['GET'])
def view_borrow_requests():
    borrow_requests = BorrowRequest.query.all()
    requests_list = [{"id": req.id, "user_id": req.user_id, "book_id": req.book_id,
                      "start_date": req.start_date, "end_date": req.end_date, "status": req.status} for req in borrow_requests]
    return jsonify(requests_list)

# Approve or deny borrow request
@admin_bp.route('/borrow_request/<int:id>', methods=['PUT'])
def approve_or_deny_borrow_request(id):
    request_data = request.get_json()
    status = request_data.get('status')
    
    if not status:
        return jsonify({"message": "Status is required"}), 400
    
    borrow_request = BorrowRequest.query.get(id)
    
    if not borrow_request:
        return jsonify({"message": "Borrow request not found"}), 404
    
    borrow_request.status = status
    db.session.commit()
    
    return jsonify({"message": f"Borrow request {status} successfully"}), 200
