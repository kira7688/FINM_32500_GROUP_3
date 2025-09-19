from datetime import datetime



class Order:
    # make this immutable
    def __init__(self, symbol: str, quantity: int, price: float, status: str):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.status = status

class MarketDataPoint:
    # make this immutable
    def __init__(self, timestamp: datetime, symbol: str, price: float):
        self.timestamp = timestamp
        self.symbol = symbol
        self.price = price



    
