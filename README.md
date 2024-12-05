
 
# Library Management System

This is a library management system built with Flask and SQLAlchemy. It includes functionality for librarians to manage users and book borrow requests, and for users to borrow books.

## Setup

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Initialize the database: `python database.py` and 'setup_db.py'
4. Run the app: `python app.py`.
5. Access the APIs at 27.0.0.1:5000          
 {<Rule '/api/admin/create_user' (POST, OPTIONS) -> admin_bp.create_user>,
 <Rule '/api/admin/borrow_requests' (GET, OPTIONS, HEAD) -> admin_bp.view_borrow_requests>,
 <Rule '/api/admin/borrow_request/<id>' (OPTIONS, PUT) -> admin_bp.approve_or_deny_borrow_request>,
 <Rule '/api/user/books' (GET, OPTIONS, HEAD) -> user_bp.get_books>,
 <Rule '/api/user/borrow_request' (POST, OPTIONS) -> user_bp.borrow_book>,
 <Rule '/api/user/download_borrow_history' (GET, OPTIONS, HEAD) -> user_bp.download_borrow_history>,}
`

