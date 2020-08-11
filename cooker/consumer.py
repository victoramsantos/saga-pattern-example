import json

from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer('food_topic', bootstrap_servers=['localhost:9092'])

    for message in consumer:
        d = json.loads(message.value.decode('utf-8'))
        print(d)
