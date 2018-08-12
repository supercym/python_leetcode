# Author: cym


def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        a = list(s)
        a_reverse = a[::-1]
        count = 0
        flag = False
        for i, v in enumerate(a_reverse):
            if not v.isspace():
                count += 1
                flag = True
            elif flag is True:
                break
        return count

if __name__ == "__main__":
    print(lengthOfLastWord("hello worlds"))
    print(lengthOfLastWord(" hello worlds "))
    print(lengthOfLastWord("hello"))
    print(lengthOfLastWord("hello  "))
    print(lengthOfLastWord("  hello  "))
    print(lengthOfLastWord(" "))
