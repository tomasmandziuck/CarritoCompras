from flask import Blueprint, jsonify
from .. import mongo

products_bp = Blueprint("products", __name__)

@products_bp.route("/", methods=["GET"])
def get_products():
    products = mongo.db.productos.find()
    product_list = [
        {"id": str(product["_id"]), "name": product["name"], "price": product["price"], "imgUrl": product["imgurl"]}
        for product in products
    ]
    return jsonify(product_list), 200
