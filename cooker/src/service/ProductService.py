from typing import List

from src.model.Food import Product
from src.repository.dao.BartenderDao import BartenderDao
from src.repository.dao.BalconyDao import CookerDao
from src.repository.dao.FoodDao import ProductDao


class ProductService:
    def __init__(self, product_dao: ProductDao, cooker_dao: CookerDao, bartender_dao: BartenderDao):
        self.__product_dao = product_dao
        self.__cooker_dao = cooker_dao
        self.__bartender_dao = bartender_dao

    def get_products(self) -> List[Product]:
        products: List[Product] = self.__product_dao.list()
        return products

    def order(self, items):
        foods, drinks = self.__split_items(items)

        self.__cooker_dao.publish(foods)
        self.__bartender_dao.publish(drinks)

    def __split_items(self, items):
        foods = []
        drinks = []

        for item in items:
            if item["type"] == "FOOD":
                foods.append(item)
            else:
                drinks.append(item)

        return foods, drinks
