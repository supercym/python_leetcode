# Author: cym

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # i, j = 0, 0
        # charPos = {}
        # maxlength = 0
        # while j < len(s):
        #     if s[j] in charPos.keys() and charPos[s[j]] >= i:
        #         maxlength = max(maxlength, j-i)
        #         i = charPos[s[j]]+1
        #     charPos[s[j]] = j
        #     j += 1
        # maxlength = max(maxlength, j-i)
        # return maxlength

        i, j = 0, -1 ##滑动窗口位于[i,j]
        chars = set()
        maxlength = 0
        while i < len(s):
            if j+1 < len(s) and s[j+1] not in chars:
                j += 1
                chars.add(s[j])
            else:
                chars.remove(s[i])
                i += 1

            maxlength = max(maxlength, j-i+1)
        return maxlength

            

