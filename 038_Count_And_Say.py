# Author: cym


def countAndSay(n):

    tmp = [1]
    for i in range(n-1):
        tmp = geneNext(tmp)
    ans = [str(x) for x in tmp]
    ans = "".join(ans)
    return ans


def geneNext(tmp):
    count = 0
    val = tmp[0]
    ans = []
    for i, v in enumerate(tmp):

        if v == val:
            count += 1
        else:
            ans.append(count)
            ans.append(val)
            count = 1
            val = v

        if i == len(tmp) - 1:
            ans.append(count)
            ans.append(val)

    return ans

print(1, countAndSay(1))
print(2, countAndSay(2))
print(3, countAndSay(3))
print(4, countAndSay(4))
print('###################')
print(geneNext([1]))
print('###################')
print(geneNext([1, 1]))
print('###################')
print(geneNext([2, 1]))
print('###################')
print(geneNext([1, 2, 1, 1]))
print('###################')
print(geneNext([1, 1, 1, 2, 2, 1]))
