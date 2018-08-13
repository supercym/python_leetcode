# Author: cym


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    m = len(digits)

    d = digits
    d[m-1] += 1
    for i in range(m):
        index = m-1-i
        if d[index] < 10:
            break
        elif index != 0:
            d[index] = 0
            d[index-1] += 1
        else:
            d[index] = 1
            d.append(0)

    return d

if __name__ == "__main__":
    print(plusOne([0]))
    print(plusOne([1, 2, 3, 4]))
    print(plusOne([1, 2, 3, 9]))
    print(plusOne([1, 2, 9, 9]))
    print(plusOne([1, 9, 9, 9]))
    print(plusOne([9, 9, 9, 9]))



