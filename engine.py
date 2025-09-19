# import the models and strategies

from strategies import moving_average, momentum
from models import Order

moving_average_signal, momentum_signal = [], []

portfolio = {} # symbol -> quantity, avg price
def execute_order(order: Order, portfolio: dict):
    if order.symbol not in portfolio:
        portfolio[order.symbol] = {'quantity': 0, 'avg_price': 0.0, 'pnl': 0.0}

    if order.status == "BUY" :
        cur_quantity = portfolio[order.symbol]['quantity']
        cur_avg_price = portfolio[order.symbol]['avg_price']
        new_quantity = cur_quantity + order.quantity
        new_avg_price = (cur_quantity * cur_avg_price + order.quantity * order.price) / new_quantity

        portfolio[order.symbol] = {'quantity': new_quantity, 'avg_price': new_avg_price, 'pnl': portfolio[order.symbol]['pnl']}
    
    elif order.status == "SELL" :
        cur_quantity = portfolio[order.symbol]['quantity']
        cur_avg_price = portfolio[order.symbol]['avg_price']

        
        if order.quantity > cur_quantity:
            raise ValueError(f"Cannot sell more than current holdings for {order.symbol}, current holdings: {cur_quantity}") # raise an error or just print and move on without doing anything
        
        new_quantity = cur_quantity - order.quantity
        pnl = (order.price - cur_avg_price) * order.quantity

        portfolio[order.symbol] = {'quantity': new_quantity, 'avg_price': cur_avg_price, 'pnl': portfolio[order.symbol]['pnl'] + pnl}
    
    return portfolio

# need to get the market data points from a continous buffer 
# we are creating an engine here, not a function

# initialize market_data_points from a continous buffer (like using yield)

# for each tick 
for tick in market_data_points: # ensure that market_data_points are in timestamp order
    # Invoke each strategy to generate signals.
    ma_signal = moving_average(tick)
    mom_signal = momentum(tick)

    # Instantiate and validate Order objects.
    if ma_signal[0] != None:
        ma_order = Order( ma_signal[0], ma_signal[1], ma_signal[2], ma_signal[3] ) # initialize order with checks with timestamp

    if mom_signal[0] != None:
        mom_order = Order( mom_signal[0], mom_signal[1], mom_signal[2], mom_signal[3] ) # initialize order with checks

    # Execute orders
    portfolio = execute_order(ma_order, portfolio)
    portfolio = execute_order(mom_order, portfolio)






    



portfolio = {}





