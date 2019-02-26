# Author: cym

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        ## http://bookshadow.com/weblog/2015/06/03/leetcode-contains-duplicate-iii/
        if len(nums) < 2 or k < 1 or t <0:
            return False
        d = collections.OrderedDict()
        for i in range(len(nums)):
            key = int(nums[i]/max(1, t))
            for p in {key-1, key, key+1}:
                if p in d.keys() and abs(nums[i]-d[p]) <= t:
                    return True
            d[key] = nums[i]
            if i >= k:
                d.popitem(last=False)

        return False
