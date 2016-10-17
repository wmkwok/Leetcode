# Given an array and a value, remove all instances of that value in place and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example:
# Given input array nums = [3,2,2,3], val = 3

# Your function should return length = 2, with the first two elements of nums being 2.

# Hint:
# Try two pointers.
# Did you use the property of "the order of elements can be changed"?
# What happens when the elements to remove are rare?

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        end = 0
        for i in range(1, len(nums)):
            if nums[end] != val:
                end += 1
            if i != end:
                nums[end] = nums[i]

        if end == val:
            nums[end] = None
        size = end + 1
        end += 1
        while end < len(nums):
            nums[end] = None
            end += 1
        print nums
        return size

sol = Solution()
test = [1, 1, 2, 2, 2, 2, 3, 4]
print sol.removeElement(test, 2)
