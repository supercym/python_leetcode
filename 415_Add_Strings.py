# Author: cym

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        stradd = {}
        for i in range(0, 11):
            for j in range(0, 11):
                stradd[(i, j)] = ((i+j) % 10, (i+j)//10)

        length = max(len(num1), len(num2))
        if len(num1) < length:
            num1 = num1.zfill(length)
        else:
            num2 = num2.zfill(length)

        ans = []
        k = 0
        for c in range(length):
            s1, s2 = stradd[(int(num1[length-c-1]), int(num2[length-c-1]))]
            s1 += k
            if s1 == 10:
                s1 = 0
                s2 = 1
            k = s2
            ans.append(str(s1))
        if k != 0:
            ans.append(str(k))
        ans = ans[::-1]
        return "".join(ans)
