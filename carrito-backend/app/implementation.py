# Initialices mongo database with its collections
def initialice_mongo(mongo):
    #Check if the collections already exists
    if "products" not in mongo.db.list_collection_names():
            mongo.db.create_collection("products")
    if "users" not in mongo.db.list_collection_names():
            mongo.db.create_collection("users") 

    #Check if the collection is empty 
    if mongo.db.products.count_documents({}) == 0:
        #insert the base products
        mongo.db.products.insert_many([{
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
            }])
    return True