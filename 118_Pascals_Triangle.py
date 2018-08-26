# Author: cym

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ans = []
        tmp = [1]
        ans.append(tmp)
        while numRows != 1:
            tmp = self.gene_row(tmp)
            ans.append(tmp)
            numRows -= 1
        return ans


    def gene_row(self, row):
        next_row = [1]
        for i in range(len(row)):
            if i == len(row) - 1:
                next_row.append(1)
            else:
                next_row.append(row[i] + row[i+1])
        return next_row

