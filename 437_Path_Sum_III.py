# Author: cym

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        def dsf(root, target):
            res = 0
            if root is None:
                return res
            if root.val == target:
                res += 1
            res += dsf(root.left, target-root.val)
            res += dsf(root.right, target-root.val)
            return res
        return dsf(root, sum)+self.pathSum(root.left, sum)+self.pathSum(root.right, sum)

