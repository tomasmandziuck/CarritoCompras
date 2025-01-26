from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from .. import mongo
import logging as logger

auth_bp = Blueprint("auth", __name__)

logger.basicConfig(filename="carrito.log", level=logger.INFO)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    # Verifica si el usuario ya existe
    if mongo.db.users.find_one({"email": email}):
        return jsonify({"message": "User already exists"}), 400

    # Registra al usuario
    hashed_password = generate_password_hash(password)
    mongo.db.users.insert_one({"email": email, "password": hashed_password})

    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = mongo.db.users.find_one({"email": email})

    logger.info(password)
    logger.info(user["password"])
    logger.info(check_password_hash(user["password"], password))
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"message": "Invalid email or password"}), 401

    # Genera un token JWT
    access_token = create_access_token(identity=str(user["_id"]))
    return jsonify({"access_token": access_token}), 200