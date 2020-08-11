import os

from src.library.database.Mongo import Mongo
from src.model.product.Product import Product


class ProductDao:
    def __init__(self):
        self.__mongo: Mongo = Mongo(
            host=os.getenv("MONGO_HOST"),
            port=int(os.getenv("MONGO_PORT")),
            default_db=os.getenv("MONGO_INITDB_DATABASE")
        )
        self.__products = os.getenv("MONGO_PRODUCTS_DB")
        self.__customerOrders = os.getenv("MONGO_CUSTOMER_ORDERS_DB")

    def list(self):
        arr = []
        for product in self.__mongo.find_all(self.__products):
            arr.append(self.__build_product(product))

        return arr

    @staticmethod
    def __build_product(elem) -> Product:
        return Product(
            name=elem["name"],
            type=elem["type"],
            id=int(elem["id"])
        )