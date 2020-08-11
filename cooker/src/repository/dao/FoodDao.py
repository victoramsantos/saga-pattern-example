import os

from src.library.database.Mongo import Mongo
from src.model.Food import Food


class FoodDao:
    def __init__(self):
        self.__mongo: Mongo = Mongo(
            host=os.getenv("MONGO_HOST"),
            port=int(os.getenv("MONGO_PORT")),
            default_db=os.getenv("MONGO_INITDB_DATABASE")
        )
        self.__foods = os.getenv("MONGO_FOODS_DB")

    def find_by_id(self, id: int):
        food = []
        for elem in self.__mongo.find_by(self.__foods, {"id": id}):
            food.append(
                Food(
                    id=int(elem["id"]),
                    timer=int(elem["timer"])
                )
            )

        return food[0]