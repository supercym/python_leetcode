# Author: cym

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(low, high):
            index = low
            ref = nums[low]
            for i in range(low, high+1):
                if nums[i] >= ref:
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1
            nums[low], nums[index-1] = nums[index-1], nums[low]
            return index-1

        l, h = 0, len(nums)-1
        ref = -1
        while l <= h:
            ref = nums[l]
            res = partition(l, h)
            if res == k-1:
                break
            elif res > k-1:
                h = res-1
            elif res < k-1:
                l = res+1
        return ref
