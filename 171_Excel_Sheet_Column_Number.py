# Author: cym

def titleToNumber(s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in range(1, 27):
            d[chr(i+64)] = i

        val = 0
        index = 0
        s = s[::-1]
        for c in s:
            val += d[c]*pow(26, index)
            index += 1
        return val


if __name__ == "__main__":
    print(titleToNumber("Z"))
    print(titleToNumber("AB"))
