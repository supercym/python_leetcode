# Author: cym

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for _, v in enumerate(nums):
            if v in d.keys():
                d[v] += 1
            else:
                d[v] = 1
        ans = 0
        max_count = 0
        for k, v in d.items():
            if v > max_count:
                max_count = v
                ans = k
        return ans


