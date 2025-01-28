from flask import Flask, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from . import implementation as imp


jwt = JWTManager()
mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    # Configuración
    app.config["MONGO_URI"] = "mongodb://root:test@carrito-db:27017/carrito_db?authSource=admin"
    #app.config["MONGO_URI"] = "mongodb://localhost:27017/carrito_db"
    app.config["JWT_SECRET_KEY"] = "the_project_key"

    CORS(app, supports_credentials=True)  

    mongo.init_app(app)
    jwt.init_app(app)

    response = imp.initialice_mongo(mongo)



    """ if "productos" not in mongo.db.list_collection_names():
            mongo.db.create_collection("productos")
    if "users" not in mongo.db.list_collection_names():
            mongo.db.create_collection("users")        

    if mongo.db.productos.count_documents({}) == 0:
        mongo.db.productos.insert_many([{
            "name": "Control",
            "price": 160,
            "imgurl": "./images/control.png"
            },
            {
            "name": "Monitor",
            "price": 500,
            "imgurl": "./images/monitor.png"
            },
            {
            "name": "Auriculares",
            "price": 90,
            "imgurl": "./images/auriculares.png"
            },
            {
            "name": "Teclado",
            "price": 60,
            "imgurl": "./images/teclado.png"
            },
            {
            "name": "Mouse",
            "price": 30,
            "imgurl": "./images/mouse.png"
            }]) """
        
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