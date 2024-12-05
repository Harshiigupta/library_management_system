# from app import db
# from models import User, Book

# def init_db():
#     db.create_all()

#     # Adding some books (if you want to prepopulate data)
#     book1 = Book(title="Python 101", author="John Doe", isbn="123456")
#     book2 = Book(title="Flask for Beginners", author="Jane Doe", isbn="789101")
#     db.session.add_all([book1, book2])
#     db.session.commit()

# init_db()



# from flask_sqlalchemy import SQLAlchemy

# # Initialize db object
# db = SQLAlchemy()

# def init_db(app):
#     # Bind the app to db
#     db.init_app(app)
#     db.create_all()  # Create the 



# from database import db
# from app import app

# def init_db():
#     db.init_app(app)
#     db.create_all()
#     print("Database initialized!")

# # Call this to initialize the DB
# init_db()
from flask_sqlalchemy import SQLAlchemy

# Initialize db object
db = SQLAlchemy()

def init_db():
    # We don't need to call this in the main app file anymore. This is handled inside create_app.
    pass

