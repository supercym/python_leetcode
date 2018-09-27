# Author: cym

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = list(s)
        a = a[::-1]
        ans = "".join(a)
        return ans



