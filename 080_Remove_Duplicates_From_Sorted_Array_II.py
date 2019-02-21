# Author: cym

class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0:
            return 0
        i, j = 0, 0
        val = nums[0]
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
                if count <= 2:
                    nums[j] = nums[i]
                    j += 1

            else:
                val = nums[i]
                nums[j] = nums[i]
                j += 1
                count = 1
        return j
