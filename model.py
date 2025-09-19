import time
import datetime
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

#Custom Exceptions

class OrderError(Exception):
    """Exception raised for invalid order parameters."""
    pass

class ExecutionError(Exception):
    """Exception raised during order execution failures."""
    pass

class StrategyError(Exception):
    """Exception raised for strategy-related errors."""
    pass

@dataclass(frozen=True)  # This makes it IMMUTABLE
class MarketDataPoint:
    timestamp: datetime.datetime
    symbol: str
    price: float
    
    def __post_init__(self):
        if self.price <= 0:
            raise ValueError(f"Price must be positive, got {self.price}")

class OrderStatus(Enum):
    PENDING = "PENDING"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"

class OrderType(Enum):
    BUY = "BUY"
    SELL = "SELL"

class Order:    
    def __init__(self, symbol, quantity, price, order_type):
        self._validate_order_params(symbol, quantity, price, order_type)
        
        self.symbol = symbol.strip().upper()
        self.quantity = int(quantity)
        self.price = float(price)
        self.order_type = order_type if isinstance(order_type, OrderType) else OrderType(order_type.upper())
        
        self.status = OrderStatus.PENDING
        self.created_at = datetime.datetime.now()
        self.filled_at = None
        self.fill_price = None
        self.rejection_reason = None
    
    @staticmethod
    def _validate_order_params(symbol, quantity, price, order_type):
        if not symbol or not isinstance(symbol, str):
            raise OrderError("Symbol must be a non-empty string")
        
        if quantity <= 0:
            raise OrderError(f"Quantity must be positive, got {quantity}")
        
        if price <= 0:
            raise OrderError(f"Price must be positive, got {price}")
        
        if isinstance(order_type, str):
            order_type = order_type.upper()
            if order_type not in ("BUY", "SELL"):
                raise OrderError("Order type must be 'BUY' or 'SELL'")
        elif not isinstance(order_type, OrderType):
            raise OrderError("Order type must be OrderType enum or string")
    
    def value(self):
        #total order value.
        return self.quantity * self.price
    
    def summary(self):
        """Print order summary."""
        print(f"{self.order_type.value} {self.quantity} shares of {self.symbol} "
              f"at ${self.price:.2f} each. Total: ${self.value():,.2f}")
    
    #Order lifecycle methods
    def fill(self, fill_price: float) -> None:
        if self.status != OrderStatus.PENDING:
            raise OrderError(f"Cannot fill order with status {self.status}")
        
        self.status = OrderStatus.FILLED
        self.filled_at = datetime.datetime.now()
        self.fill_price = fill_price
    
    def cancel(self) -> None:
        if self.status != OrderStatus.PENDING:
            raise OrderError(f"Cannot cancel order with status {self.status}")
        
        self.status = OrderStatus.CANCELLED
    
    def reject(self, reason: str = "Unknown") -> None:
        self.status = OrderStatus.REJECTED
        self.rejection_reason = reason
    
    def __repr__(self) -> str:
        return (f"Order({self.order_type.value} {self.quantity} {self.symbol} "
                f"@ ${self.price:.2f}, Status: {self.status.value})")

#OrderBook
class OrderBook:    
    def __init__(self):
        self.orders = []   

    def add_order(self, order):
        self.orders.append(order)

    def get_orders_by_symbol(self, symbol):
        sym = symbol.strip().upper()
        return [o for o in self.orders if o.symbol == sym]

    def total_volume(self, side):
        if isinstance(side, str):
            side = side.upper()
            order_type = OrderType.BUY if side == "BUY" else OrderType.SELL
        else:
            order_type = side
    
        return sum(o.quantity for o in self.orders if o.order_type == order_type)
