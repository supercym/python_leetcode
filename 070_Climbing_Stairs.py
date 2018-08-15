# Author: cym


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    # *********  Low Efficient  *************
    # if n > 2:
    #     total = climbStairs(n-1) + climbStairs(n-2)
    # elif n == 2:
    #     return 2
    # else:
    #     return 1
    # return total
    # *********  High Efficient  *************
    d = {1: 1, 2: 2, 3: 3}
    if n < 4:
        return d[n]
    m = 4
    while m <= n:
        d[m] = d[m-1] + d[m-2]
        m += 1
    return d[n]


if __name__ == "__main__":
    print(climbStairs(35))
