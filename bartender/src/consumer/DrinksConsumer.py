import json
import os

from kafka import KafkaConsumer

from src.model.Drink import Drink
from src.model.DrinkRequest import DrinkRequest
from src.model.OrderRequest import OrderRequest
from src.repository.dao.BalconyDao import BalconyDao
from src.repository.dao.DrinkDao import DrinkDao


class DrinksConsumer:
    def __init__(self, drink_dao: DrinkDao, balcony_dao: BalconyDao):
        self.__topic = KafkaConsumer(
            os.getenv("KAFKA_TOPIC_DRINK"),
            bootstrap_servers=[os.getenv("KAFKA_SERVER")]
        )
        self.__balcony_dao = balcony_dao
        self.__drink_dao = drink_dao

    def consumes(self):
        for message in self.__topic:
            drink_request_blob = json.loads(message.value.decode('utf-8'))
            self.cook(DrinksConsumer.parse_drink_request(drink_request_blob))

    def cook(self, order: OrderRequest):
        for item in order.items:
            drink: Drink = self.__drink_dao.find_by_id(item.id)
            drink.cook()
            self.__balcony_dao.publish({
                "orderId": order.order_id,
                "item": drink.__dict__
            })

    @staticmethod
    def parse_drink_request(request):
        return OrderRequest(
            order_id=int(request["orderId"]),
            items=[
                DrinkRequest(
                    id=item["id"],
                    type=item["type"]
                ) for item in request["items"]
            ]
        )
