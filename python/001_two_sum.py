# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution0(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i] + nums[j] == target:
                        return [i, j]


nums = [2, 7, 11, 15]
target = 9
sol0 = Solution0()
print sol0.twoSum(nums, target)

class Solution1(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if dict.has_key(target-nums[i]):
                return (dict[target-nums[i]][1], i)
            else:
                dict.setdefault(nums[i], (target-nums[i], i))

sol1 = Solution1()
print sol1.twoSum(nums, target)
