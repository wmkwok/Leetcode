class Solution():
    def two_sum(self, l, time):
        dict = {}
        for each in l:
            if (time - each) in dict.keys():
                return True
            else:
                dict[each] = time - each
        return False



sol = Solution()
test = [1, 2, 4, 7]
num = 10
print sol.two_sum(test, num)
