# Author: cym
class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        l, h = 0, len(nums)-1
        while l < h:
            m = int(l + (h-l)/2)
            if nums[m] == nums[m+1]:
                if m % 2 == 1:
                    h = m-1
                else:
                    l = m+2
            elif nums[m] == nums[m-1]:
                if m % 2 == 1:
                    l = m+1
                else:
                    h = m-2
            else:
                return nums[m]
        return nums[h]



