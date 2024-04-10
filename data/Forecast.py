from dataclasses import dataclass


@dataclass
class Forecast:
    description: str
    temperature: float
    feels_like: float
    wind_speed: float
