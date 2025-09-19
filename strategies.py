from abc import ABC, abstractmethod
from models import MarketDataPoint

class Strategy(ABC):
    @abstractmethod
    def generate_signals(self, tick: MarketDataPoint) -> list:
        pass

class MovingAverageStrategy(Strategy):
    def __init__(self, window: int = 5):
        self._window = window
        self._prices = []

    def generate_signals(self, tick: MarketDataPoint) -> list:
        self._prices.append(tick.price)
        if len(self._prices) > self._window:
            self._prices.pop(0)

        if len(self._prices) == self._window:
            avg_price = sum(self._prices) / self._window
            if tick.price > avg_price:
                return ["BUY"]  # give the quantity to place an order here
            elif tick.price < avg_price:
                return ["SELL"] # give the quantity to place an order here
        return [None]