# Author: cym

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False

        if root.left is None and root.right is None and root.val == sum:
            return True

        hasLeftPath = self.hasPathSum(root.left, sum - root.val)
        hasRightPath = self.hasPathSum(root.right, sum - root.val)

        return hasLeftPath or hasRightPath
