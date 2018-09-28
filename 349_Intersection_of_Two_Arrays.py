# Author: cym

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # ans = []
        # d1 = dict.fromkeys(nums1, 0)
        # d2 = dict.fromkeys(nums2, 0)
        # for k in d1.keys():
        #     if k in d2.keys():
        #         ans.append(k)
        # return ans

        ans = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans

