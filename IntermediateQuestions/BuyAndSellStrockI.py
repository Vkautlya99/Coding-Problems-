# Description: Given an array of prices, find the maximum profit that can be made by buying and selling a stock at most once.


def BuyAndSellStock(Prices):
    max_profit = 0
    for i in range(len(Prices)):
        for j in range(i+1, len(Prices)):
            profit = Prices[j] - Prices[i]
            max_profit = max(max_profit, profit)
    return max_profit

Prices = [7, 1, 5, 3, 6, 4]
print(BuyAndSellStock(Prices))
    

#METHOD : 2 - Greedy algorith approach 

def BuyAndSellStockByGreedyAlgorith(PriceArray):
    min_price = float('inf')
    max_profit = 0
    
    for price in PriceArray:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
        
    return max_profit

Prices = [7, 1, 5, 3, 6, 4]
print(BuyAndSellStockByGreedyAlgorith(Prices))




