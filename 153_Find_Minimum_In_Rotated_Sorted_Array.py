# Author: cym
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums)-1
        while l < h:
            m = int(l+(h-l)/2)
            if nums[m] < nums[h]:
                h = m
            elif nums[m] > nums[l]:
                l = m
            else:
                break
        return nums[h]


