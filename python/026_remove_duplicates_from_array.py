# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

class Solution():
    def __init__(self, array):
        self.array = array

    def solve(self):
        i = 0
        j = 1
        arr = self.array

        while j < len(arr):
            if arr[i] == arr[j]:
                j += 1
            elif arr[i] < arr[j]:
                i += 1
                arr[i] = arr[j]
            else: # arr[i] > arr[j]:
                j += 1

        return i + 1

