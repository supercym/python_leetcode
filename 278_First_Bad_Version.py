# Author: cym

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        low = 1
        high = n
        while high - low > 1:
            mid = int((low + high) / 2)
            if isBadVersion(mid):
                high = mid
            else:
                low = mid
        return high

