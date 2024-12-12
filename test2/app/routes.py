from flask import Blueprint, jsonify, request
from .models import products, get_next_id

api_blueprint = Blueprint("api", __name__)

# Create a new product
@api_blueprint.route("/", methods=["POST"])
def add_product():
    data = request.json
    if not data.get("name") or not data.get("price"):
        return jsonify({"error": "Product name and price are required"}), 400
    
    new_product = {
        "id": get_next_id(),
        "name": data["name"],
        "price": data["price"],
        "description": data.get("description", "")
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Retrieve all products
@api_blueprint.route("/", methods=["GET"])
def get_products():
    return jsonify(products), 200

# Retrieve a single product by ID
@api_blueprint.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

# Update a product by ID
@api_blueprint.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    data = request.json
    product["name"] = data.get("name", product["name"])
    product["price"] = data.get("price", product["price"])
    product["description"] = data.get("description", product.get("description", ""))
    return jsonify(product), 200

# Delete a product by ID
@api_blueprint.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    global products
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    products = [p for p in products if p["id"] != product_id]
    return jsonify({"message": "Product deleted successfully"}), 200
