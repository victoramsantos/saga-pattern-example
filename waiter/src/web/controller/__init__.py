from src.repository.dao.CookerDao import CookerDao
from src.repository.dao.ProductDao import ProductDao
from src.service.ProductService import ProductService

product_dao: ProductDao = ProductDao()

cooker_dao: CookerDao = CookerDao()

service: ProductService = ProductService(
    product_dao=product_dao,
    cooker_dao=cooker_dao
)
