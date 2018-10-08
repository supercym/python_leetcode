# Author: cym

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c in s:
            try:
                d[c] += 1
            except KeyError:
                d[c] = 1
        count = 0
        Odd = False
        for k, v in d.items():
            if v % 2 == 0:
                count += v
            elif v >= 3:
                count += v-1
                Odd = True
            else:
                Odd = True
        return count+1 if Odd else count

