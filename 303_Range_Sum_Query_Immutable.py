# Author: cym

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

        if len(nums) > 0:
            self.d = {}
            self.d[0] = self.nums[0]
            for i in range(1, len(self.nums)):
                self.d[i] = self.d[i-1] + self.nums[i]


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.d[j]
        return self.d[j] - self.d[i-1]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

