from dataclasses import dataclass
import datetime
import time
import csv
from typing import List

@dataclass(frozen=True)
class MarketDataPoint:
    timestamp: datetime.datetime
    symbol: str
    price: float


def read_market_data(
        input_file_loc: str,
) -> List[List[str]]:
    """
    Reads market data CSV file and returns a list of input data rows.

    :param input_file_loc: Path to input CSV file.

    """
    with open(input_file_loc, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        reader = list(reader)

    return reader


def parse_market_data(
    input_file_loc: str,
) -> List[MarketDataPoint]:
    """
    Reads and parses market data CSV file and returns a list of MarketDataPoint.

    :param input_file_loc: Path to input CSV file.

    """
    try:
        reader = read_market_data(input_file_loc)
    except Exception as e:
        print(e)
        return []

    parsed_data = []
    for row in reader[1:]:
        (timestamp, symbol, price) = row
        timestamp = datetime.datetime.fromisoformat(timestamp)
        price = float(price)

        parsed_data.append(MarketDataPoint(
            timestamp=timestamp,
            symbol=symbol,
            price=price
        ))

    return parsed_data

if __name__ == "__main__":
    # Example: read market_data.csv file
    input_file_loc = "market_data.csv"

    parsed_data = parse_market_data(input_file_loc=input_file_loc)

    print(f"{input_file_loc} parsed with {len(parsed_data)} rows")