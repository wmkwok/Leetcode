#Say you have an array for which the ith element is the price of a given stock on day i.

#If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find themaximum profit.

#Example 1:
#Input: [7, 1, 5, 3, 6, 4]
#Output: 5

#max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
#Example 2:
#Input: [7, 6, 4, 3, 1]
#Output: 0

#In this case, no transaction is done, i.e. max profit = 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxp = 0
        p1 = 0
        p2 = 1
        while p2 < len(prices):
            if prices[p2] > prices[p1]:
                maxp = max(maxp, prices[p2] - prices[p1]);
                p2 += 1
            else:
                p1 = p2
                p2 += 1
        return maxp

sol = Solution()
test = [10, 7, 5, 8, 11, 9]
print sol.maxProfit(test)
