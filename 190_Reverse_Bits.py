# Author: cym

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # n_bin = bin(n)[2:].zfill(32)
        # n_revese_bin = n_bin[::-1]
        # n_reverse = int(n_revese_bin, 2)
        # return n_reverse

        value = 0
        mask = 1
        for i in range(32):
            value = (value << 1) | ((n & mask) >> i)
            mask <<= 1
        return value
