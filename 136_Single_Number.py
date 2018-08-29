# Author: cym

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = nums[0]
        for i in range(1, len(nums)):
            tmp ^= nums[i]
        return tmp
