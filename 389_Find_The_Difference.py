# Author: cym

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ds = {}
        for c in s:
            try:
                ds[c] += 1
            except KeyError:
                ds[c] = 1
        dt = {}
        for c in t:
            try:
                dt[c] += 1
            except KeyError:
                dt[c] = 1
        for k, v in dt.items():
            if k not in ds.keys():
                return k
            if v != ds[k]:
                return k

