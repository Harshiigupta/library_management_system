from app import create_app
from database import db
from models import User, Book, BorrowRequest
import datetime  # Import the datetime module

# Create an app instance
app = create_app()

# Push the app context to interact with the database
with app.app_context():
    # Add users
    user1 = User(email="alice@example.com", password="password123")
    user2 = User(email="bob@example.com", password="password456")
    db.session.add(user1)
    db.session.add(user2)

    # Add books
    book1 = Book(title="The Catcher in the Rye", author="J.D. Salinger", isbn="978-0-316-76948-0")
    book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", isbn="978-0-06-112008-4")
    book3 = Book(title="1984", author="George Orwell", isbn="978-0-452-28423-4")
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)

    db.session.commit()  # Commit to get the IDs of users and books


    # Add borrow requests (using Python date objects instead of strings)
    borrow_request1 = BorrowRequest(
        user_id=user1.id, 
        book_id=book1.id, 
        start_date=datetime.date(2024, 12, 5),  # Convert string to date object
        end_date=datetime.date(2024, 12, 12),    # Convert string to date object
        status="Pending"
    )
    borrow_request2 = BorrowRequest(
        user_id=user2.id, 
        book_id=book2.id, 
        start_date=datetime.date(2024, 12, 6),  # Convert string to date object
        end_date=datetime.date(2024, 12, 13),    # Convert string to date object
        status="Pending"
    )
    db.session.add(borrow_request1)
    db.session.add(borrow_request2)

    # Commit the changes to the database
    db.session.commit()

    print("Sample data added to the database successfully!")
