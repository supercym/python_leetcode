# Author: cym


def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """

        s = {n}
        while True:
            val = 0
            while n != 0:
                remainder = n % 10
                val += pow(remainder, 2)
                n //= 10

            if val == 1:
                return True
            if val in s:
                return False
            else:
                s.add(val)
            n = val



if __name__ == "__main__":
    print(isHappy(19))




