from app import create_app, db
from models import User, BorrowRequest, Book

# Create the Flask app
app = create_app()

# Push the application context
with app.app_context():
    # Query the User table
    print("Users in the database:", User.query.all())

    # Query the BorrowRequest table
    print("Borrow Requests in the database:", BorrowRequest.query.all())
