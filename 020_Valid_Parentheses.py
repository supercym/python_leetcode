# Author: cym


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if s is None:
        return True
    if len(s) % 2 == 1:
        return False
    d = {"(": 1, ")": -1, "[": 2, "]": -2, "{": 3, "}": -3}
    n = [d[x] for x in s]
    tmp = []
    for i in range(len(n)):
        if len(tmp) != 0 and tmp[len(tmp)-1] + n[i] == 0:
            tmp.pop()
        else:
            tmp.append(n[i])
    return len(tmp) == 0


print(isValid("()"))
print('###################')
print(isValid("()[]{}"))
print('###################')
print(isValid("(]"))
print('###################')
print(isValid("([)]"))
print('###################')
print(isValid("{[]}"))
