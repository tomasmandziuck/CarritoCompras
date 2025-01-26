from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from .. import mongo

cart_bp = Blueprint("cart", __name__)

""" @cart_bp.route("/add", methods=["POST"])
def add_to_cart():
    data = request.json
    user_id = data.get("user_id")
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    cart = mongo.db.carts.find_one({"user_id": user_id})
    if not cart:
        mongo.db.carts.insert_one({"user_id": user_id, "items": []})

    mongo.db.carts.update_one(
        {"user_id": user_id, "items.product_id": {"$ne": product_id}},
        {"$addToSet": {"items": {"product_id": product_id, "quantity": quantity}}},
        upsert=True
    )
    return jsonify({"message": "Product added to cart"}), 200

@cart_bp.route("/summary", methods=["GET"])
def cart_summary():
    user_id = request.args.get("user_id")
    cart = mongo.db.carts.find_one({"user_id": user_id})
    if not cart:
        return jsonify({"message": "Cart is empty", "total": 0, "items": []}), 200

    items = cart.get("items", [])
    total = sum(item["quantity"] * mongo.db.productos.find_one({"_id": item["product_id"]})["price"] for item in items)
    return jsonify({"items": items, "total": total}), 200 """


@cart_bp.route("/add", methods=["POST"])
@jwt_required()
def add_to_cart():
    """
    Adds a product to the user's cart or updates the quantity if the product already exists.
    """
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
    """
    Returns the cart summary for the user, including total price and number of items.
    """
    user_id = get_jwt_identity()
    cart = mongo.db.cart.find_one({"user_id": user_id})

    if not cart or "products" not in cart:
        return jsonify({"total_items": 0, "total_price": 0.0}), 200

    total_items = sum(product["quantity"] for product in cart["products"])
    total_price = sum(product["quantity"] * product["price"] for product in cart["products"])

    return jsonify({"total_items": total_items, "total_price": total_price}), 200