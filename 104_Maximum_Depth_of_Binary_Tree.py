# Author: cym

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left_depth = 1 + self.maxDepth(root.left)
        right_depth = 1 + self.maxDepth(root.right)

        return max(left_depth, right_depth)
