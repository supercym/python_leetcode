# Author: cym

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: x[1])
        people = sorted(people, key=lambda x: x[0], reverse=True)
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans


