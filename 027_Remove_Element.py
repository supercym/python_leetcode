# Author: cym
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a = 0
        b = 0
        for i in range(len(nums)):
            if nums[i] == val:
                a += 1
            else:
                nums[i-a] = nums[i]
                b += 1
        return b
