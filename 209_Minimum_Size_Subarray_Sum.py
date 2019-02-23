# Author: cym

class Solution:
    def minSubArrayLen(self, s: 'int', nums: 'List[int]') -> 'int':
        if len(nums) == 0:
            return 0
        i, j = 0, 0
        sumij = nums[0] ## sum between nums[i, j]
        arrlen = len(nums)+1

        while True:
            if sumij >= s:
                arrlen = min(arrlen, j-i+1)
                if i == j:
                    break
                else:
                    sumij -= nums[i]
                    i += 1
            else:
                if j == len(nums)-1:
                    break
                j += 1
                sumij += nums[j]

        if arrlen == len(nums)+1:
            return 0

        return arrlen



