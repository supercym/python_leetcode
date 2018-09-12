# Author: cym

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for v in nums:
            if v not in d.keys():
                d[v] = 0
            else:
                return True
        return False
