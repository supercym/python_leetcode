# Author: cym

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        dRan = {}
        for c in ransomNote:
            try:
                dRan[c] += 1
            except KeyError:
                dRan[c] = 1

        dMag = {}
        for c in magazine:
            try:
                dMag[c] += 1
            except KeyError:
                dMag[c] = 1

        for k, v in dRan.items():
            if k not in dMag.keys():
                return False
            if v > dMag[k]:
                return False
        return True
    

