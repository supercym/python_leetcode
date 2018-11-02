# Author: cym

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        h = sorted(intervals, key=lambda x: x.end)
        ans = [h[0]]
        while True:
            lastIntervals = ans[-1]
            ansLength = len(ans)
            for t in h:
                if t.start >= lastIntervals.end:
                    ans.append(t)
                    break
            if len(ans) == ansLength:
                break
        return len(intervals)-len(ans)




