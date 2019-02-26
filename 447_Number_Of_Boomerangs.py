# Author: cym

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for p in points:
            dis = {}
            for q in points:
                d = math.pow(p[0]-q[0], 2)+math.pow(p[1]-q[1], 2)
                if d in dis.keys():
                    dis[d] += 1
                else:
                    dis[d] = 1
            for _, v in dis.items():
                ans += v*(v-1)
        return ans
