# Author: cym

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = set("aeiouAEIOU")
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] not in d:
                i += 1
            elif s[j] not in d:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)


