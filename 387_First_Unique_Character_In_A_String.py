# Author: cym

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i, c in enumerate(s):
            if c not in d.keys():
                d[c] = i
            else:
                d[c] = len(s)
        min_index = len(s)
        for _, v in d.items():
            min_index = min(min_index, v)
        return -1 if min_index == len(s) else min_index


