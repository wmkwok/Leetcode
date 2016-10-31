#  Say you have an array for which the ith element is the price of a given stock on day i. 
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again). 


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxp = 0
        localMax = 0
        sell = 0
        p1 = 0
        p2 = 1
        while p2 < len(prices):
            if prices[p2] < prices[p1]:
                p1 += 1
                p2 += 1
            else:
                while p2 < len(prices) and localMax < prices[p2]-prices[p1]:
                    localMax = prices[p2] - prices[p1]
                    p2 += 1
                maxp += prices[p2-1] - prices[p1]
                localMax = 0
                p1 = p2
                p2 += 1

        return maxp


sol = Solution()
test = [10, 7, 5, 8, 11, 9]
test1 = [1, 3, 4, 10, 5, 9, 7, 5, 15]
print sol.maxProfit(test)
print sol.maxProfit(test1)
