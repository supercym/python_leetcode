# Author: cym

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        low = 1
        high = n
        while True:
            if guess(high) == 0:
                ans = high
                break
            mid = int((low+high)/2)
            g = guess(mid)
            if g == 0:
                ans = mid
                break
            elif g == -1:
                high = mid
            elif g == 1:
                low = mid
        return ans


