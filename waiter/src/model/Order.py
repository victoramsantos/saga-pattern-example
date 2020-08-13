from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Order:
    order_id: int
    item_id: int
    status: str = ""
