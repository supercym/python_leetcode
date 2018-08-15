# Author: cym
import math


def mySqrt(x):
    if x == 0:
        return 0
    ans = x
    while True:
        tmp = 0.5 * (ans + (x / ans))
        if abs(tmp - ans) < 1:
            break
        else:
            ans = tmp
    return int(tmp)


if __name__ == "__main__":
    print(mySqrt(4))
    print(math.sqrt(4))
    print(mySqrt(1836583659))
    print(math.sqrt(1836583659))




