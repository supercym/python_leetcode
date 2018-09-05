# Author: cym

class Solution:
    # def rotate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     if k > len(nums):
    #         k %= len(nums)
    #     tmp = nums[len(nums)-k:len(nums)]
    #     for i in range(len(nums)-k):
    #         nums[len(nums)-1-i] = nums[len(nums)-k-1-i]
    #     for i in range(len(tmp)):
    #         nums[i] = tmp[i]


    # ***********  reverse 3 times  ***************
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k > length:
            k %= length

        self.reverse(nums, 0, length-k-1)
        self.reverse(nums, length-k, length-1)
        self.reverse(nums, 0, length-1)


    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
