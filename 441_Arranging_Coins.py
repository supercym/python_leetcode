# Author: cym

class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        from math import sqrt
        k = int((sqrt(8*n+1)-1)/2)
        while True:
            tempSum = int(k*(k+1)/2)
            if tempSum == n:
                ans = k
                break
            elif tempSum > n:
                ans = k-1
                break
            k += 1
        return ans

