# Author: cym
class Solution:
    def twoSum(self, nums, target):
        """
        hahaha
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, val in enumerate(nums):
            temp = target - val
            for j in range(i+1, len(nums)):
                if nums[j] == temp:
                    ans = [i, j]
                    return ans
        return 0
