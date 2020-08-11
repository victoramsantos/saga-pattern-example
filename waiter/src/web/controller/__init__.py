from src.repository.dao.BartenderDao import BartenderDao
from src.repository.dao.CookerDao import CookerDao
from src.repository.dao.ProductDao import ProductDao
from src.service.ProductService import ProductService

product_dao: ProductDao = ProductDao()

cooker_dao: CookerDao = CookerDao()
bartender_dao: BartenderDao = BartenderDao()

service: ProductService = ProductService(
    product_dao=product_dao,
    cooker_dao=cooker_dao,
    bartender_dao=bartender_dao
)
