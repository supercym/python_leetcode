# Author: cym
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = list('IVXLCDM')
        b = [1, 5, 10, 50, 100, 500, 1000]
        d = dict(zip(a, b))
        num = [d[x] for x in s]
        if len(num) == 1:
            return num[0]
        for i in range(len(num)-1):
            if num[i] < num[i+1]:
                num[i] = -num[i]
        return sum(num)
