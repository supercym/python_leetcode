# Author: cym

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        low, high = -1, len(nums)
        index = 0
        while index < high:
            if nums[index] == 0:
                low += 1
                nums[low], nums[index] = nums[index], nums[low]
                index = low+1
            elif nums[index] == 2:
                high -= 1
                nums[high], nums[index] = nums[index], nums[high]
            else:
                index += 1
        return
