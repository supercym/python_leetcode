# Author: cym

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        record = dict()

        for i in range(h-1, -1, -1):
            for j in range(i+1):
                if i == h-1:
                    record[(i, j)] = triangle[i][j]
                else:
                    record[(i, j)] = triangle[i][j] + min(record[(i+1, j)], record[(i+1, j+1)])

        return record[(0, 0)]

