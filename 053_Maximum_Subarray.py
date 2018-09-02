# Author: cym


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # *******    Kadene Algorithm   ***********
        # max_sum = nums[0]
        # if len(nums) > 1:
        #     tmp_sum = 0
        #     for i in range(len(nums)):
        #         tmp_sum += nums[i]
        #         if tmp_sum > max_sum:
        #             max_sum = tmp_sum
        #         if tmp_sum < 0:
        #             tmp_sum = 0
        # return max_sum

        # *******    Divide & Conquer Approach   ***********
        length = len(nums)
        if length == 1:
            return nums[0]

        mid = length//2
        left = self.maxSubArray(nums[:mid])
        right = self.maxSubArray(nums[mid:])

        s1 = nums[mid-1]
        left_sum = 0
        for i in nums[:mid][::-1]:
            left_sum += i
            if left_sum > s1:
                s1 = left_sum

        s2 = nums[mid]
        right_sum = 0
        for j in nums[mid:]:
            right_sum += j
            if right_sum > s2:
                s2 = right_sum

        sum_val = s1+s2
        if sum_val < left:
            sum_val = left
        if sum_val < right:
            sum_val = right
        return sum_val
