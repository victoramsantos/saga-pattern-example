from dataclasses import dataclass
import time

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Drink:
    id: int
    timer: int

    def cook(self):
        time.sleep(self.timer)