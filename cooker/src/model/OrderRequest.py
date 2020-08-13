from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from src.model.FoodRequest import FoodRequest


@dataclass_json
@dataclass
class OrderRequest:
    order_id: int
    items: List[FoodRequest]