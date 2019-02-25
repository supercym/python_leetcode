# Author: cym

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        n = len(A)
        d1, d2 = {}, {}
        for i in range(n):
            for j in range(n):
                if A[i]+B[j] in d1.keys():
                    d1[A[i]+B[j]] += 1
                else:
                    d1[A[i]+B[j]] = 1

                if C[i]+D[j] in d2.keys():
                    d2[C[i]+D[j]] += 1
                else:
                    d2[C[i]+D[j]] = 1

        ans = 0
        for k1, v1 in d1.items():
            if -k1 in d2.keys():
                ans += v1*d2[-k1]
        return ans

