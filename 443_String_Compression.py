# Author: cym

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        start, end = 0, 0
        while True:
            if chars[start] == chars[end]:
                end += 1
                if end != len(chars):
                    continue
            length = end - start
            if length > 1:
                tmp = []
                while length != 0:
                    tmp.append(str(length % 10))
                    length //= 10
                tmp = tmp[::-1]
                chars[start+1:end] = tmp[:]
                end = start+1+len(tmp)
            start = end
            if end == len(chars):
                break
        return len(chars)

