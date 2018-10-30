# Author: cym

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}
        maxCount = 0
        for n in nums:
            try:
                counter[n] += 1
            except KeyError:
                counter[n] = 1
            if counter[n] > maxCount:
                maxCount = counter[n]

        barrels = [[] for _ in range(maxCount)]

        for key, v in counter.items():
            barrels[v-1].append(key)

        ans = []
        for i in range(maxCount-1, -1, -1):
            ans.extend(barrels[i])
            if len(ans) >= k:
                break
        return ans


