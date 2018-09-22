# Author: cym

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = len(nums)
        for i in range(len(nums)):
            ans ^= i
            ans ^= nums[i]
        return ans

            
