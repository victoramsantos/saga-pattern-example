from src.repository.dao.BalconyDao import BalconyDao

from src.consumer.BalconyConsumer import BalconyConsumer
from src.repository.dao.ProductDao import ProductDao

balcony_dao = BalconyDao()
product_dao = ProductDao()

balcony_consumer = BalconyConsumer(product_dao, balcony_dao)
