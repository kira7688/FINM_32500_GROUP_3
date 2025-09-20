# models.py
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True, slots=True)
class Order:
    symbol: str
    quantity: int
    price: float
    status: str = "NEW"  # default; still immutable

@dataclass(frozen=True, slots=True)
class MarketDataPoint:
    timestamp: datetime
    symbol: str
    price: float
