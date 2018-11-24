# Author: cym
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                cnt += 1
                if (i-2) < 0 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return cnt <= 1

