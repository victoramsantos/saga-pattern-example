from typing import List

from src.model.Product import Product
from src.repository.dao.CookerDao import CookerDao
from src.repository.dao.ProductDao import ProductDao


class ProductService:
    def __init__(self, product_dao: ProductDao, cooker_dao: CookerDao):
        self.__product_dao = product_dao
        self.__cooker_dao = cooker_dao

    def get_products(self) -> List[Product]:
        products: List[Product] = self.__product_dao.list_products()
        return products

    def make_items(self, order):
        foods = self.order(order)

        self.register_items(foods)

    def register_items(self, items):
        order_status = self.build_order_status(items)
        for item in order_status:
            self.__product_dao.add_item(item)

    def order(self, order):
        foods = ProductService.__split_items(order)

        self.__cooker_dao.publish(foods)

        return foods

    @staticmethod
    def build_order_status(order):
        return [
            {
                "orderId": int(order["orderId"]),
                "itemId": int(item["id"]),
                "status": "PENDING"
            } for item in order["items"]
        ]

    @staticmethod
    def __split_items(order):
        foods = []

        for item in order["items"]:
            if item["type"] == "FOOD":
                foods.append(item)

        return {
                   "orderId": int(order["orderId"]),
                   "items": foods
               }

    def get_orders(self):
        orders = self.__product_dao.list_orders()
        return orders
