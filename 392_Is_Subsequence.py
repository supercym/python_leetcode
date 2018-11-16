# Author: cym

class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        index = 0
        count = 0
        for c in s:
            while t[index] != c:
                index += 1
                if index == len(t):
                    return False
            count += 1
            index += 1
            if index == len(t) and count != len(s):
                    return False
        return True

        

