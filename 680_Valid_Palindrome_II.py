# Author: cym

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(t):
            i, j = 0, len(t)-1
            while i < j:
                if t[i] != t[j]:
                    return False
                i += 1
                j -= 1
            return True
        res = True
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                if isPalindrome(s[i+1:j+1]) or isPalindrome(s[i:j]):
                    res = True
                else:
                    res = False
                break
            i += 1
            j -= 1
        return res

