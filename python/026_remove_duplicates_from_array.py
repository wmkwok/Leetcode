# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[end]:
                end += 1
            if i != end:
                nums[end] = nums[i]
        size = end + 1
        end += 1
        while end < len(nums):
            nums[end] = None
            end += 1
        print nums
        return size

sol = Solution()
test = [1, 1, 2 ,3, 4]
print sol.removeDuplicates(test)
