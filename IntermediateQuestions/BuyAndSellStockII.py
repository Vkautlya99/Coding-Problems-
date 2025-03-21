#You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete at most two transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



def BuyandSellStockII(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            first_profit = max(0, prices[j] - prices[i])
            for k in range(j + 1, len(prices)):
                for l in range(k + 1, len(prices)):
                    second_profit = max(0, prices[l] - prices[k])
                    max_profit = max(max_profit, first_profit + second_profit)
    return max_profit

prices = [3,3,5,0,0,3,1,4]
print(BuyandSellStockII(prices)) 


# METHOD : 2 - Using Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(1) 
def SellandBuyStockIIByDP(pricearray):
    buy1 , buy2 = float('inf'), float('inf')    
    profit1, profit2 = 0, 0
    
    for price in pricearray:
        buy1 = min(buy1, price)
        profit1 = max(profit1, price - buy1)
        
        buy2 = min(buy2, price - profit1)
        profit2 = max(profit2, price - buy2)
        
    return profit2
prices = [3,3,5,0,0,3,1,4]
print(BuyandSellStockII(prices))       
   

