# Author: cym

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        mask = 1
        i = 0
        while i < 32:
            if num == mask << i:
                return True
            i += 2
        return False

