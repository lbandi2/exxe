from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class Step:
    date: datetime
    status: str
    message: str


class Tracking:
    def __init__(self, steps: List) -> None:
        self.parsed_steps = steps
    
    @property
    def list(self) -> List:
        return [Step(*item) for item in self.parsed_steps]