# Author: cym

class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        ans = 0
        flag = True
        for c in s:
            if c != " " and flag:
                ans += 1
                flag = False
            elif c == " ":
                flag = True
        return ans


