# Author: cym

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        k = num
        while abs(k*k - num) > 1:
            k = 0.5 * (k + num/k)
        k = int(k)
        if k*k == num or (k-1)*(k-1) == num or (k+1)*(k+1) == num:
            return True
        else:
            return False


