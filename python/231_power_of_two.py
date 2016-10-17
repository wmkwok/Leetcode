# Given an integer, write a function to determine if it is a power of two.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n > 0) and ((n & (n - 1)) == 0)

sol = Solution()
test = 16
test1 = 14
print sol.isPowerOfTwo(test)
print sol.isPowerOfTwo(test1)
