# Author: cym

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        total_profit = 0
        buy = prices[0]
        sold = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy and buy == sold:
                buy = prices[i]
                sold = prices[i]
            elif prices[i] >= sold:
                sold = prices[i]
                if i == len(prices)-1:
                    total_profit += (sold - buy)
            elif prices[i] < sold and prices[i-1] == sold:
                total_profit += (sold - buy)
                buy = prices[i]
                sold = prices[i]
        return total_profit
