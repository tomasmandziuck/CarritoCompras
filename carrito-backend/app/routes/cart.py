import requests
from flask import Blueprint, jsonify, request

cart_bp = Blueprint("cart", __name__)


@cart_bp.route("/shipping-options", methods=["POST"])
def get_shipping_options():

    data = request.get_json()
    cart_total = data.get("cart_total")

    if cart_total is None:
        return jsonify({"message": "Cart total is required"}), 400

    # Call Go microservice
    go_service_url = "http://carrito-shipping:8080/shipping-options"
    try:
        response = requests.post(go_service_url, json={"cart_total": cart_total})
        response.raise_for_status()
        shipping_options = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"message": "Error fetching shipping options", "error": str(e)}), 500

    return jsonify({"shipping_options": shipping_options}), 200