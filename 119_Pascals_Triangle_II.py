# Author: cym

def getRow(rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        mid = int(rowIndex/2)
        ans = [0] * (rowIndex+1)
        for i in range(mid+1):
            ans[i] = combi(rowIndex, i)
            ans[rowIndex-i] = ans[i]
        return ans


def combi(a, b):
    if b == 0:
        return 1
    numerator = factorial(a)
    denominator = factorial(b) * factorial(a-b)
    return int(numerator/denominator)


def factorial(a):
    if a == 1:
        return a
    else:
        return a * factorial(a-1)

if __name__ == "__main__":
    print(getRow(0))
    print(getRow(1))
    print(getRow(2))
    print(getRow(3))
