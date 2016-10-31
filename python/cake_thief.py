class Solution(object):
    def maxValue(self, size, cakes):
        value = 0
        while (0,0) in cakes:
            cakes.pop(cakes.index((0,0)))
            
        ratios = [(cake[1]/cake[0], cake[0]) for cake in cakes]

        
        while len(ratios) != 0 and size != 0:

            maxValue = max(ratios)
            value += (size/maxValue[1])*maxValue[1]*maxValue[0]
            print value
            size %= maxValue[1]
            ratios.pop(ratios.index(maxValue))
        return value


sol = Solution()
test = [(7, 160), (3, 90), (2, 15)]
print sol.maxValue(20, test)
