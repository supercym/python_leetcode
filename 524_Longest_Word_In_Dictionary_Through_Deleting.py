# Author: cym

class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        maxLength = 0
        res = ""
        for t in d:
            if len(t) < maxLength or (len(t) == maxLength and t > res):
                continue
            if self.isValid(s, t):
                maxLength = len(t)
                res = t
        return res

    def isValid(self, target, s):
        if len(target) < len(s):
            return False
        i, j = 0, 0
        while i < len(target) and j < len(s):
            if s[j] == target[i]:
                j += 1
            i += 1
        return j == len(s)
        

