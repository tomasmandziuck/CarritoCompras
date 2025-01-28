from bson.objectid import ObjectId

class User:
    collection_name = "users"

    @staticmethod
    def to_dict(user):
        return {
            "_id": str(user["_id"]),
            "email": user["email"],
            "password": user["password"]
        }

class Product:
    collection_name = "products"

    @staticmethod
    def to_dict(product):
        return {
            "_id": str(product["_id"]),
            "name": product["name"],
            "price": product["price"]
        }