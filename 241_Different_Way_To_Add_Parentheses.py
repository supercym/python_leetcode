# Author: cym

class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        s = input
        ans = []
        for i in range(len(s)):
            if s[i] == "+" or s[i] == "-" or s[i] == "*":
                left = self.diffWaysToCompute(s[:i])
                right = self.diffWaysToCompute(s[i+1:])
                for l in left:
                    for r in right:
                        if s[i] == "+":
                            ans.append(l+r)
                        elif s[i] == "-":
                            ans.append(l-r)
                        else:
                            ans.append(l*r)
        if len(ans) == 0:
            return [int(s)]
        return ans 
