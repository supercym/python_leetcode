# Author: cym

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                ans = s if abs(target-s) < abs(target-ans) else ans
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s
        return ans
                    


