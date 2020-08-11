from src.consumer.FoodsConsumer import FoodsConsumer
from src.repository.dao.BalconyDao import BalconyDao
from src.repository.dao.FoodDao import FoodDao

balcony_dao = BalconyDao()
food_dao = FoodDao()

foods_consumer = FoodsConsumer(food_dao, balcony_dao)