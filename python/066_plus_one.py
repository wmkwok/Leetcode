# Given a non-negative number represented as an array of digits, plus one to the number.
# The digits are stored such that the most significant digit is at the head of the list.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        mult = 1
        for i in range(len(digits)-1, -1, -1):
            sum += mult * ((int)(digits[i]))
            mult *= 10
        return sum+1


test1 = "1234567890"
sol = Solution()
print sol.plusOne(test1)
