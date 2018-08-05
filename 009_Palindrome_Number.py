# Author: cym
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        c = [n for n in list(str(x))]
        d = c[::-1]
        return c == d
