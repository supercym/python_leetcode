# Author: cym


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) == 0:
        return 0
    ans = -1
    for i in range(len(haystack) - len(needle) + 1):
        tmp = [haystack[i+j] == needle[j] for j in range(len(needle))]
        if len(needle) == sum(tmp):
            ans = i
            break
    return ans


print(strStr("hello", "ll"))
print('###################')
print(strStr("favorite", "te"))
print('###################')
print(strStr("helllllo", "ll"))
print('###################')
print(strStr("hello", "ad"))
print('###################')
print(strStr("hello", ""))

