# Author: cym

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s = [str(x) for x in range(1, n+1)]
        for i in range(2, n, 3):
            s[i] = "Fizz"
        for i in range(4, n, 5):
            s[i] = "Buzz"
        for i in range(14, n, 15):
            s[i] = "FizzBuzz"
        return s


