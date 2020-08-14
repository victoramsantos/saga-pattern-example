import os

from src.library.database.Mongo import Mongo
from src.model.Drink import Drink


class DrinkDao:
    def __init__(self):
        self.__mongo: Mongo = Mongo(
            host=os.getenv("MONGO_HOST"),
            port=int(os.getenv("MONGO_PORT")),
            default_db=os.getenv("MONGO_INITDB_DATABASE")
        )
        self.__drinks = os.getenv("MONGO_DRINKS_DB")

    def find_by_id(self, id: int):
        drink = []
        for elem in self.__mongo.find_by(self.__drinks, {"id": id}):
            drink.append(
                Drink(
                    id=int(elem["id"]),
                    timer=int(elem["timer"])
                )
            )

        return drink[0]