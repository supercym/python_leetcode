# Author: cym

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        ds = {}
        dt = {}
        for i in range(len(s)):
            try:
                ds[s[i]] += 1
            except:
                ds[s[i]] = 1
        for i in range(len(t)):
            try:
                dt[t[i]] += 1
            except:
                dt[t[i]] = 1
        for k, v in ds.items():
            if k not in dt.keys():
                return False
            if v != dt[k]:
                return False
        return True


