# Author: cym
class Solution:
    def geneCom(self, upperBound, n):
        ans = []
        for i in range(upperBound):
            mask = 1
            count = 0
            for _ in range(6):
                if i & mask == mask:
                    count += 1
                mask <<= 1
            if count == n:
                ans.append(i)
        return ans


    def geneHM(self, n):
        ans = []
        for i in range(4):
            if 0 <= n - i <= 5:
                ans.append((i, n-i))
        return ans


    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        HM = self.geneHM(num)
        for v in HM:
            h = self.geneCom(12, v[0])
            m = self.geneCom(60, v[1])
            t = [str(x)+":"+str(y).zfill(2) for x in h for y in m]
            ans.extend(t)
        return ans

