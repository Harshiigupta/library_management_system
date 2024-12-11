from flask import Flask, render_template
#from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from database import db  # Import db from the database.py
# from routes.admin_routes import admin_bp  # Import your admin routes blueprint
# from routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'supersecretkey'

    # Initialize extensions
    db.init_app(app)  # Initialize db here
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    # Register blueprints after app is created
    from routes.admin_routes import admin_bp  # Import routes here
    from routes.user_routes import user_bp  # Import routes here

    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(user_bp, url_prefix='/api/user')

    # Add a route for the dashboard
    @app.route('/')
    def dashboard():
        return render_template('dashboard.html')  # Render the main dashboard page

    return app  # Return the app instance
    

if __name__ == '__main__':
    app = create_app()  # Call the factory function to create the app
    print(app.url_map)  # Print the URL map to see all available routes
    app.run(debug=True)
    with app.app_context():
       db.create_all()  # Create all tables














# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_jwt_extended import JWTManager
# from routes.admin_routes import admin_bp
# from routes.user_routes import user_bp # type: ignore
# from database import db

# app = Flask(__name__)

# # Database configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['JWT_SECRET_KEY'] = 'supersecretkey'

# # Initialize extensions
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# jwt = JWTManager(app)

# # Register blueprints
# app.register_blueprint(admin_bp, url_prefix='/api/admin')
# app.register_blueprint(user_bp, url_prefix='/api/user')

# if __name__ == '__main__':
#     app.run(debug=True)

