from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import jsonify, request

def authenticate_user(email, password):
    # Dummy authentication (you should hash and compare passwords)
    if email == "admin@library.com" and password == "password":
        return True
    return False
