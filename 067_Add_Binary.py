# Author: cym


def addBinary(a, b):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    c = [int(x) for x in a]
    d = [int(x) for x in b]

    c_val = 0
    for i, v in enumerate(c):
        c_val += v * (1 << (len(c)-1-i))

    d_val = 0
    for i, v in enumerate(d):
        d_val += v * (1 << (len(d)-1-i))

    val = c_val + d_val
    bin_val = bin(val)
    ans = bin_val[2:]
    return ans

if __name__ == "__main__":
    a = '1010'
    b = '1011'
    print(addBinary('1010', '1011'))
    print(addBinary('11', '1'))



