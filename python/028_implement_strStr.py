# Implement strStr().
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i

sol = Solution()
haystack = "dsdaabcd"
needle = "abc"
print sol.strStr(haystack, needle)     
