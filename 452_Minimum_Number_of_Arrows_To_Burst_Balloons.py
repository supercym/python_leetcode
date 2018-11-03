# Author: cym

class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 0:
            return 0
        spans = sorted(points, key=lambda x:x[1])
        span = spans[0]
        cnt = 1
        for t in spans:
            if t[0] > span[1]:
                span = t
                cnt += 1
        return cnt

