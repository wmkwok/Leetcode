class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if len(str) < 2:
            return False
        double = str*2
        return (str in double[1:-1])



sol = Solution()
print sol.repeatedSubstringPattern("ababc")
