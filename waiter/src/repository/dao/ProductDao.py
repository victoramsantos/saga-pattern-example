import os

from src.library.database.Mongo import Mongo
from src.model.Order import Order
from src.model.Product import Product


class ProductDao:
    def __init__(self):
        self.__mongo: Mongo = Mongo(
            host=os.getenv("MONGO_HOST"),
            port=int(os.getenv("MONGO_PORT")),
            default_db=os.getenv("MONGO_INITDB_DATABASE")
        )
        self.__products = os.getenv("MONGO_PRODUCTS_DB")
        self.__customerOrders = os.getenv("MONGO_CUSTOMER_ORDERS_DB")

    def list_products(self):
        arr = []
        for product in self.__mongo.find_all(self.__products):
            arr.append(self.__build_product(product))

        return arr

    def list_orders(self):
        arr = []
        for order in self.__mongo.find_all(self.__customerOrders):
            arr.append(self.__build_order(order))

        return arr

    def add_item(self, item):
        self.__mongo.insert_one(
            collection=self.__customerOrders,
            elem=item
        )

    def update_item(self, order_id, item_id, status):
        self.__mongo.update_one(
            query={
                "itemId": item_id,
                "orderId": order_id
            },
            collection=self.__customerOrders,
            value={"status": status}
        )

    @staticmethod
    def __build_product(elem) -> Product:
        return Product(
            name=elem["name"],
            type=elem["type"],
            id=int(elem["id"])
        )

    @staticmethod
    def __build_order(elem) -> Order:
        return Order(
            order_id=int(elem["orderId"]),
            item_id=int(elem["itemId"]),
            status=elem["status"]
        )
