# Author: cym

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        count = [True] * n
        count[0], count[1] = False, False
        # 我们只需遍历[2,sqrt(n)],因为超过sqrt(n)部分如果不是素数，则作为因子在前面的数已经被删除了
        for i in range(2, int(n**0.5)+1):
            if count[i]:
                count[i*i: n: i] = [False] * len(count[i*i: n: i])
        return sum(count)
