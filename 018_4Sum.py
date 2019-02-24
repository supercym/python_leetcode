# Author: cym

class Solution:
    def fourSum(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':
        nums.sort()
        length = len(nums)
        ans = []
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, length-1
                while l < r:
                    s = nums[l]+nums[r]
                    if s < target-nums[i]-nums[j]:
                        l += 1
                    elif s > target-nums[i]-nums[j]:
                        r -= 1
                    else:
                        if l > j+1 and nums[l] == nums[l-1]:
                            l, r = l+1, r-1
                        else:
                            ans.append([nums[i], nums[j], nums[l], nums[r]])
                            l, r = l+1, r-1
        return ans


                

