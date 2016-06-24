
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev_roman = 0
        cur_roman = 0
        total = 0
        for i in range(len(s)-1, -1, -1):
            prev_roman = cur_roman
            if s[i].upper() == 'I':
                cur_roman = 1
            if s[i].upper() == 'V':
                cur_roman = 5
            if s[i].upper() == 'X':
                cur_roman = 10
            if s[i].upper() == 'L':
                cur_roman = 50
            if s[i].upper() == 'C':
                cur_roman = 100
            if s[i].upper() == 'M':
                cur_roman = 1000
            
            if cur_roman < prev_roman:
                total -= cur_roman
            else:
                total += cur_roman
                
        return total
            

test1 = "III"  #3
test2 = "IV"   #4
test3 = "lxix" #69
test4 = "MMMCMXCIX"
sol = Solution()
print sol.romanToInt(test1)
print sol.romanToInt(test2)
print sol.romanToInt(test3)
print sol.romanToInt(test4)        
