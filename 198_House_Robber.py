# Author: cym

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 迭代，时间复杂度很高，原因在于有很多地方重复计算
        # 哪些地方重复计算了呢，可以思考一下070爬楼梯的问题为什么使用迭代效率很低
        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) == 2:
        #     return max(nums[0], nums[1])
        # if len(nums) == 3:
        #     return max(nums[0] + nums[2], nums[1])
        # if len(nums) >= 4:
        #     return max(nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))

        # 动态规划，到第i点为止的最大值val(i)等于max(val(i-1), val(i-2)+nums[i])
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        val_2 = nums[0]
        val_1 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            val_cur = max(val_1, val_2 + nums[i])
            val_2 = val_1
            val_1 = val_cur

        return val_1
