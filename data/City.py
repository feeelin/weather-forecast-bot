from pydantic.dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class City(BaseModel):
    name: str
    lon: float
    lat: float
    country: str
