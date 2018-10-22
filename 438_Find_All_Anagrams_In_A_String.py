# Author: cym

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        # pChar表示窗口内距离满足要求的字符串还多pChar[c]个c
        pChar = Counter(p)
        lenp = len(p)
        count = lenp
        ans = []
        for i in range(len(s)):
            if pChar[s[i]] >= 1:
                count -= 1
            pChar[s[i]] -= 1
            if i >= lenp:
                if pChar[s[i-lenp]] >= 0:
                    count += 1
                pChar[s[i-lenp]] += 1
            if count == 0:
                ans.append(i-lenp+1)
        return ans
