# Author: cym


def convertToTitle(n):
        """
        :type n: int
        :rtype: str
        """
        alpha = [chr(i) for i in range(65, 91)]
        d = {}
        for i in range(1, 26):
            d[i] = alpha[i-1]
        d[0] = "Z"

        s = []
        while True:
            a = n % 26
            b = (n-a) // 26
            s.append(d[a])
            if a == 0:
                b -= 1
            if b == 0:
                break
            elif b < 26:
                s.append(d[b])
                break
            elif b == 26:
                s.append(d[0])
                break
            else:
                n = b
        s = s[::-1]
        ans = "".join(s)
        return ans


if __name__ == "__main__":

    print(convertToTitle(26))  # Z
    print(convertToTitle(28))  # AB
    print(convertToTitle(77))  # BY
    print(convertToTitle(78))  # BZ
