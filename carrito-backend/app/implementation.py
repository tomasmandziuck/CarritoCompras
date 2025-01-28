def initialice_mongo(mongo):
    if "productos" not in mongo.db.list_collection_names():
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
            }])
    return True