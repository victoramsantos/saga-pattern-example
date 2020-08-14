from src.consumer.DrinksConsumer import DrinksConsumer
from src.repository.dao.BalconyDao import BalconyDao
from src.repository.dao.DrinkDao import DrinkDao

balcony_dao = BalconyDao()
drink_dao = DrinkDao()

drinks_consumer = DrinksConsumer(drink_dao, balcony_dao)