# Author: cym

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        while len(S):
            k = self.partition(S)
            S = S[k:]
            ans.append(k)
        return ans

    def partition(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        index = {}
        for i in range(len(S)):
            index[S[i]] = i
        subStrEnd = index[S[0]]
        pointer = 0
        while index[S[pointer]] <= subStrEnd:
            pointer += 1
            if pointer > subStrEnd:
                break
            if index[S[pointer]] > subStrEnd:
                subStrEnd = index[S[pointer]]
        return pointer



