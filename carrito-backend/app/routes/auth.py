from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from .. import mongo

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    """
    Registers a new user by saving their email and hashed password in the database.

    """
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    # Check if the user already exists
    if mongo.db.users.find_one({"email": email}):
        return jsonify({"message": "User already exists"}), 400

    # Registers user
    hashed_password = generate_password_hash(password)
    mongo.db.users.insert_one({"email": email, "password": hashed_password})

    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Authenticates a user by checking their email and password and returns a JWT token.

    """
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = mongo.db.users.find_one({"email": email})

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"message": "Invalid email or password"}), 401

    # Generates JWT token 
    access_token = create_access_token(identity=str(user["_id"]))
    return jsonify({"access_token": access_token}), 200