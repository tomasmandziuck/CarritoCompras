from flask import Blueprint, jsonify
from .. import mongo
import logging as logger

products_bp = Blueprint("products", __name__)
logger.basicConfig(filename="carrito.log", level=logger.INFO)

@products_bp.route("/", methods=["GET"])
def get_products():
    products = mongo.db.productos.find()
    logger.info(products)
    product_list = [
        {"id": str(product["_id"]), "name": product["name"], "price": product["price"], "imgUrl": product["imgurl"]}
        for product in products
    ]
    return jsonify(product_list), 200
