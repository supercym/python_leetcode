# Author: cym

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ans = 0
        emptyLen = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if i == len(flowerbed):
                    return int((i+1)/2) >= n
                emptyLen = i - 2
                break
        if emptyLen >= 0:
            ans += int(emptyLen/2)+1
        pointer = emptyLen + 2
        while pointer < len(flowerbed):
            if pointer == len(flowerbed)-1 and flowerbed[pointer] == 0 and flowerbed[pointer-1] == 0:
                ans += 1
                break
            if flowerbed[pointer] == 0 and flowerbed[pointer-1] == 0 and flowerbed[pointer+1] == 0:
                flowerbed[pointer] = 1
                ans += 1
            pointer += 1
        return ans >= n

