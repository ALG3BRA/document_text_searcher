from dataclasses import dataclass
from typing import List


@dataclass
class BaseIndexModel:
    index: str
    body_content: List[str]
