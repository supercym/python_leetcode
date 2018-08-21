# Author: cym

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        tmp1 = p
        tmp2 = q
        if tmp1 is None and tmp2 is not None:
            return False
        if tmp1 is not None and tmp2 is None:
            return False
        if tmp1 is None and tmp2 is None:
            return True

        if tmp1.val != tmp2.val:
            return False
        return self.isSameTree(tmp1.left, tmp2.left) and self.isSameTree(tmp1.right, tmp2.right)
