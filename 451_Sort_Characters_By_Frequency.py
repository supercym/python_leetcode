# Author: cym

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = {}
        maxCount = 0
        for c in s:
            try:
                counter[c] += 1
            except KeyError:
                counter[c] = 1
            if counter[c] > maxCount:
                maxCount = counter[c]

        barrels = [[] for _ in range(maxCount)]
        for k, v in counter.items():
            barrels[v-1].append(k)

        res = []
        for i in range(maxCount-1, -1, -1):
            for c in barrels[i]:
                res.extend(c*(i+1))
        return "".join(res)

