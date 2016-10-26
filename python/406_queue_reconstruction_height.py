class Solution(object):
    def reQueue(self, list):
        d = dict()
        newList = []
        for x, y in list:
            d.setdefault(y, []).append(x)
            print d[y]
        for key in d:
            for each

test = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
sol = Solution()
sol.reQueue(test)

