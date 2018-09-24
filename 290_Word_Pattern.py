# Author: cym

def wordPattern(pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p = list(pattern)
        s = str.split(" ")
        if len(p) != len(s):
            return False
        d = {}
        value_set = set()
        for i in range(len(p)):
            if p[i] in d.keys():
                if d[p[i]] != s[i]:
                    return False
            else:
                d[p[i]] = s[i]
                if s[i] in value_set:
                    return False
                else:
                    value_set.add(s[i])
        return True

