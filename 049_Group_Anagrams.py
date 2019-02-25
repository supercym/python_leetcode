# Author: cym

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            t = "".join(sorted(list(s)))
            if t in d.keys():
                d[t].append(s)
            else:
                d[t] = [s]
        ans = [v for _, v in d.items()]
        return ans
