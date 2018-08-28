# Author: cym

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        tmp = []
        for _, v in enumerate(s):
            if v.isalnum():
                if v.isupper():
                    v = v.lower()
                tmp.append(v)
        tmp_reverse = tmp[::-1]
        return tmp_reverse == tmp
