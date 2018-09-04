# Author: cym

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        tmp = n // 5
        while tmp != 0:
            count += tmp
            tmp = tmp // 5

        return count
