class Solution():
    def find_anagrams(self, s, p):
        sol = []
        dict = {}
        for i in range(len(p)):
            dict[p[i]] = dict.get(p[i], 0)-1
        
        for i in range(len(p)):
            dict[s[i]] = dict.get(s[i], 0)+1
            if dict.get(s[i], None) == 0:
                del dict[s[i]]
            if not dict:
                sol.append(0)

        for i in range(2,len(s)-1):
            dict[s[i-2]] = dict.get(s[i-2], 0)-1
            dict[s[i+1]] = dict.get(s[i+1], 0)+1
            if dict.get(s[i-2], None) == 0:
                del dict[s[i-2]]
            if dict.get(s[i+1], None) == 0:
                del dict[s[i+1]]
            if not dict:
                sol.append(i-1)
        return sol



sol = Solution()
test = "cbaebabacd"           
p = "abc"
print sol.find_anagrams(test, p)
