__author__ = 'Jia'
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices is None or len(prices) == 0:
            return 0
        before = [0] * len(prices)
        after = [0] * len(prices)
        smallest = prices[0]
        for i in range(1, len(before)):
            smallest = min(prices[i], smallest)
            before[i] = max(before[i - 1], prices[i] - smallest)
        largest = prices[-1]
        for j in range(len(after) - 2, -1, -1):
            largest = max(largest, prices[j])
            after[j] = max(after[j + 1], largest - prices[j])
        result = 0
        for i in range(len(prices)):
            result = max(result, before[i] + after[i])
        return result

