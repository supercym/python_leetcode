# Author: cym


def numSquares(n):
    sqnums = set()
    i = 1
    while True:
        if i * i < n:
            sqnums.add(i*i)
            i += 1
        elif i * i == n:
            return 1
        else:
            break
    ans = 1
    tree = sqnums
    while True:
        ans += 1
        tmpTree = set()
        for v in tree:
            for c in sqnums:
                if v + c == n:
                    return ans
                elif v + c < n:
                    tmpTree.add(v+c)
        tree = tmpTree

print(numSquares(12))
