import os

from src.library.database.Mongo import Mongo


class AppService:

    def health_checker(self):
        database_status: bool = self.__check_database()

        return database_status, {
            "mongodb_status": database_status
        }

    def __check_database(self):
        try:
            mongodb: Mongo = Mongo(
                host=os.getenv("MONGO_HOST"),
                port=int(os.getenv("MONGO_PORT")),
                default_db=os.getenv("MONGO_DEFAULT_DB")
            )
            return "ok" in mongodb.status()
        except:
            return False
