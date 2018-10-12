# Author: cym

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = set(nums)

        def findmax():
            maxV = list(snums)[0]
            for n in snums:
                if n > maxV:
                    maxV = n
            return maxV

        firstmax = findmax()
        snums.remove(firstmax)
        if len(snums) == 0:
            return firstmax

        secondmax = findmax()
        snums.remove(secondmax)
        if len(snums) == 0:
            return firstmax

        return findmax()


