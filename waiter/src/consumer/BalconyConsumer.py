import json
import os

from kafka import KafkaConsumer

from src.library.logger.Logger import Logger
from src.repository.dao.BalconyDao import BalconyDao
from src.repository.dao.ProductDao import ProductDao


class BalconyConsumer:
    def __init__(self, product_dao:ProductDao, balcony_dao: BalconyDao):
        self.__topic = KafkaConsumer(
            os.getenv("KAFKA_TOPIC_BALCONY"),
            bootstrap_servers=[os.getenv("KAFKA_SERVER")]
        )
        self.__balcony_dao = balcony_dao
        self.__product_dao = product_dao

    def consumes(self):
        for message in self.__topic:
            order_attender = json.loads(message.value.decode('utf-8'))
            self.attend(order_attender)

    def attend(self, order):
        Logger.info(f"Attending order_id={order['orderId']} item_id={order['item']['id']}")
        self.__product_dao.update_item(
            item_id=int(order["item"]["id"]),
            status="DONE"
        )
