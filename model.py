from dataclasses import dataclass
from datetime import datetime

# Immutable market data
@dataclass(frozen=True, slots=True)
class MarketDataPoint:
    timestamp: datetime
    symbol: str
    price: float

# Mutable order
class Order:
    def __init__(self, symbol: str, quantity: int, price: float, status: str = "NEW"):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.status = status

class OrderError(Exception): ...
class ExecutionError(Exception): ...
