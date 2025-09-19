def sharpe_ratio(expected_return: float, std_dev: float): 
    
    expected_return = float(expected_return)
    
    std_dev = float(std_dev)
    
    sharpe_ratio = expected_return/std_dev
    
    print(F"The sharpe ratio is {sharpe_ratio} for our strategy")
