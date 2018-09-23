# Author: cym

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        start = 0
        move = 0
        sum_move = 0
        length = len(nums)
        while True:
            if nums[i] == 0:
                move += 1
                i += 1
            else:
                if move != 0:
                    nums[start:] = nums[start+move:]
                    nums.extend([0] * move)
                    sum_move += move
                    i -= move
                    move = 0
                else:
                    start = i + 1
                    i += 1
            if i + sum_move >= length:
                break

