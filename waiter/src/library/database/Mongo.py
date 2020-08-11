from pymongo import MongoClient

from src.library.logger.Logger import Logger


class Mongo:
    def __init__(self, host: str, port: int, default_db: str):
        Logger.info(f"Connecting to mongo using host: {host} and port: {port}")
        self.__client = MongoClient(
            host=host,
            port=port
        )
        Logger.info(f"Mongo connected. Accessing database: {default_db}")
        self.__database = self.__client[default_db]
        Logger.info(f"Database connection status: {self.status()}")

    def find_all(self, collection: str):
        db_collection = self.__database[collection]
        for elem in db_collection.find():
            yield elem

    def find_by(self, collection: str, field: dict):
        db_collection = self.__database[collection]
        for elem in db_collection.find(field):
            yield elem

    def get_any(self, collection: str):
        db_collection = self.__database[collection]
        for elem in db_collection.aggregate([{'$sample': {'size': 1}}]):
            return elem

    def status(self):
        return self.__client.server_info()


if __name__ == '__main__':
    mongo = MongoClient(
        host="localhost",
        port=27018
    )
    print(mongo.server_info())
    # db = mongo["productCatalog"]
    # collection = db["productCatalog"]
    #
    # for elem in collection.aggregate([{'$sample': {'size': 1}}]):
    #     print(elem)
