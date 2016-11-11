#Given a string, sort it in decreasing order based on the frequency of characters.

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        string = ""
        for each in s:
            dict[each] = dict.get(each, 0) + 1
        while dict:
            maxnum = 0
            maxidx = ''
            for x, y in dict.items():
                if y > maxnum:
                    maxidx = x
                    maxnum = y
            string += (maxidx * maxnum)
            del dict[maxidx]
        return string

sol = Solution()
print sol.frequencySort("tree")
                
