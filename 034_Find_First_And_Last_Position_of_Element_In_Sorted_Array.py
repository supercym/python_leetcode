# Author: cym
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, h = 0, len(nums)-1
        start, end = -1, -1
        while l <= h:
            m = int(l+(h-l)/2)
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                h = m-1
            else:
                start, end = m, m
                while start > l:
                    if nums[start-1] != target:
                        break
                    else:
                        start -= 1
                while end < h:
                    if nums[end+1] != target:
                        break
                    else:
                        end += 1
                break

        return [start, end]


