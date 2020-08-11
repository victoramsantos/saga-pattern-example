import json
import os

from kafka import KafkaProducer

from src.library.logger.Logger import Logger


class BalconyDao:

    def __init__(self):
        self.__producer = KafkaProducer(
            bootstrap_servers=[os.getenv("KAFKA_SERVER")],
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        self.__balcony_topic = os.getenv("KAFKA_TOPIC_BALCONY")

    def publish(self, item):
        Logger.info(f"publishing prepared food to balcony_topic: {item}")
        self.__producer.send(
            topic=self.__balcony_topic,
            value=item.__dict__
        )