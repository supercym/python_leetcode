# Author: cym
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        a = 0
        for b in range(1, len(nums)):
            if nums[b] == nums[a]:
                continue
            else:
                nums[a+1] = nums[b]
                a += 1
        return a+1
