# Author: cym

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum_val = numbers[left] + numbers[right]
            if sum_val == target:
                break
            if sum_val < target:
                left += 1
            if sum_val > target:
                right -= 1
        return [left+1, right+1]

