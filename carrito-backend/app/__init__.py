from flask import Flask, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from . import implementation as imp
import os

jwt = JWTManager()
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
       
    # Configuration
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    CORS(app, supports_credentials=True)  

    mongo.init_app(app)
    jwt.init_app(app)

    response = imp.initialice_mongo(mongo)

        
    @app.before_request
    def handle_options_request():
        if request.method == "OPTIONS":
             return '', 204
    
    # Register Blueprints
    from .routes.products import products_bp
    from .routes.cart import cart_bp
    from .routes.auth import auth_bp

    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(cart_bp, url_prefix="/cart")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app