# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        for i in range(min([len(s) for s in strs])):
            same = True
            for s in range(len(strs) - 1):
                if strs[s][i] != strs[s+1][i]:
                    same = False
            if same:
                prefix += strs[0][i]
            else:
                break
        return prefix
            
test = ["interstellar", "interstate", "interspecies"]
sol = Solution()
print sol.longestCommonPrefix(test)
