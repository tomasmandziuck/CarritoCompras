from flask import Flask, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_jwt_extended import JWTManager

jwt = JWTManager()
mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    # Configuración
    app.config["MONGO_URI"] = "mongodb://localhost:27017/carrito_db"
    app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"
    #CORS(app, supports_credentials=True)

    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)  # Permitir solicitudes desde el frontend

    mongo.init_app(app)
    jwt.init_app(app)

    # Handle OPTIONS globally
    @app.before_request
    def handle_options_request():
        if request.method == "OPTIONS":
             return '', 204

    # Registrar Blueprints
    from .routes.products import products_bp
    from .routes.cart import cart_bp
    from .routes.auth import auth_bp

    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(cart_bp, url_prefix="/cart")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app