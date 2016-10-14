# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        paths = 0
        if n == 0:
            return 1
        elif n < 3:
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

sol = Solution()
for i in range(5):
    print sol.climbStairs(i)
        
