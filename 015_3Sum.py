# Author: cym

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        if len(nums) < 3:
            return ans
        t = 0
        while t < len(nums) and nums[t] <= 0:
            t += 1
        for i in range(t):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                s = nums[j] + nums[k]
                if s == -nums[i]:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j+1 < k and nums[j+1] == nums[j]:
                        j += 1
                    while k-1 > j and nums[k-1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
                elif s > -nums[i]:
                    k -= 1
                else:
                    j += 1
        return ans

