# Author: cym
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l = 0
        h = len(letters)-1
        while l <= h:
            m = int(l + (h-l)/2)
            if letters[m] == target:
                if m == len(letters)-1:
                    return letters[0]
                for s in range(m+1, len(letters)):
                    if letters[s] > target:
                        return letters[s]
            if letters[m] > target:
                h = m - 1
            else:
                l = m + 1
        return letters[h+1] if h < len(letters)-1 else letters[0]
        


