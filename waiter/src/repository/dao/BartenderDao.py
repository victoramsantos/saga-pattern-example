import json
import os

from kafka import KafkaProducer

from src.library.logger.Logger import Logger


class BartenderDao:

    def __init__(self):
        self.__producer = KafkaProducer(
            bootstrap_servers=[os.getenv("KAFKA_SERVER")],
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        self.__drink_topic = os.getenv("KAFKA_TOPIC_DRINK")

    def publish(self, order):
        Logger.info(f"publishing to drink_topic: {order['orderId']}")
        self.__producer.send(
            topic=self.__drink_topic,
            value=order
        )