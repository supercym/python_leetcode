# Author: cym

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        m = {}
        flag = True
        for i, v in enumerate(nums):
            if v in d.keys():
                if v in m.keys():
                    m[v] = min(i - d[v], m[v])
                else:
                    m[v] = i - d[v]
            d[v] = i
        for _, v in m.items():
            if v <= k:
                return True
        return False
