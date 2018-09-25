# Author: cym

# 面前有1,2,3 块时必胜，4块时必输
# 意味着面前有4+1，4+2，4+3块时必胜，因为可以让对方面前只有4块，
# 同样的道理类比可以知道，只要能被4整除，必输
class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0



