import requests
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from .. import mongo

cart_bp = Blueprint("cart", __name__)


@cart_bp.route("/shipping-options", methods=["POST"])
def get_shipping_options():
    
    data = request.get_json()
    cart_total = data.get("cart_total")

    if cart_total is None:
        return jsonify({"message": "Cart total is required"}), 400

    # Call Go microservice
    go_service_url = "http://localhost:8080/shipping-options"
    try:
        response = requests.post(go_service_url, json={"cart_total": cart_total})
        response.raise_for_status()
        shipping_options = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"message": "Error fetching shipping options", "error": str(e)}), 500

    return jsonify({"shipping_options": shipping_options}), 200

""" @cart_bp.route("/add", methods=["POST"])
@jwt_required()
def add_to_cart():
    user_id = get_jwt_identity()
    data = request.get_json()

    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)
    price = data.get("price")

    if not product_id or not price:
        return jsonify({"message": "Product ID and price are required"}), 400

    # Fetch the user's cart
    cart = mongo.db.cart.find_one({"user_id": user_id})

    if not cart:
        # Create a new cart for the user
        cart = {
            "user_id": user_id,
            "products": [{"product_id": product_id, "quantity": quantity, "price": price}],
        }
        mongo.db.cart.insert_one(cart)
    else:
        # Update existing cart
        products = cart["products"]
        for product in products:
            if product["product_id"] == product_id:
                product["quantity"] += quantity
                break
        else:
            # If product doesn't exist in the cart, add it
            products.append({"product_id": product_id, "quantity": quantity, "price": price})

        mongo.db.cart.update_one({"user_id": user_id}, {"$set": {"products": products}})

    return jsonify({"message": "Product added to cart"}), 200

@cart_bp.route("/summary", methods=["GET"])
@jwt_required()
def get_cart_summary():
    user_id = get_jwt_identity()
    cart = mongo.db.cart.find_one({"user_id": user_id})

    if not cart or "products" not in cart:
        return jsonify({"total_items": 0, "total_price": 0.0}), 200

    total_items = sum(product["quantity"] for product in cart["products"])
    total_price = sum(product["quantity"] * product["price"] for product in cart["products"])

    return jsonify({"total_items": total_items, "total_price": total_price}), 200 """