import json
import os

from kafka import KafkaConsumer

from src.model.Food import Food
from src.model.FoodRequest import FoodRequest
from src.model.OrderRequest import OrderRequest
from src.repository.dao.BalconyDao import BalconyDao
from src.repository.dao.FoodDao import FoodDao


class FoodsConsumer:
    def __init__(self, food_dao: FoodDao, balcony_dao: BalconyDao):
        self.__topic = KafkaConsumer(
            os.getenv("KAFKA_TOPIC_FOOD"),
            bootstrap_servers=[os.getenv("KAFKA_SERVER")]
        )
        self.__balcony_dao = balcony_dao
        self.__food_dao = food_dao

    def consumes(self):
        for message in self.__topic:
            food_request_blob = json.loads(message.value.decode('utf-8'))
            self.cook(FoodsConsumer.parse_food_request(food_request_blob))

    def cook(self, order: OrderRequest):
        for item in order.items:
            food: Food = self.__food_dao.find_by_id(item.id)
            food.cook()
            self.__balcony_dao.publish({
                "orderId": order.order_id,
                "item": food.__dict__
            })

    @staticmethod
    def parse_food_request(request):
        return OrderRequest(
            order_id=int(request["orderId"]),
            items=[
                FoodRequest(
                    id=item["id"],
                    type=item["type"]
                ) for item in request["items"]
            ]
        )
