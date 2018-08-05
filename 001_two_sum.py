# Author: cym
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, val in enumerate(nums):
            tmp = target - val
            for j in range(i+1, len(nums)):
                if nums[j] == tmp:
                    ans = [i, j]
                    return ans
        return 0
