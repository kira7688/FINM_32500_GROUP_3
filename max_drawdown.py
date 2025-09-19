def drawdown(): 
    drawdowns = []
    prices = []
    peak = price[0]
    
    max_drawdown = 0
    
    for p in prices: 
        
        if p > peak: 
            p = peak 
            
    drawdown = ((peak-p)/peak)
    drawdowns.append(drawdown)
    
    if drawdown > max_drawdown: 
        
        max_drawdown = drawdown
        
        
    Print(F"The current maximum drawdown is {max_drawdown}"
    Print(F"The current drawdown indexed by a single unit of time is {drawdowns}"
