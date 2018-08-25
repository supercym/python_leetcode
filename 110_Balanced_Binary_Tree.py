# Author: cym

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        que = [root]
        while len(que) != 0:
            node = que[0]
            que = que[1:]

            left_depth = self.treeDepth(node.left)
            right_depth = self.treeDepth(node.right)

            if abs(left_depth - right_depth) > 1:
                return False

            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
        return True

    def treeDepth(self, root):
        if root is None:
            return 0

        left_depth = 1 + self.treeDepth(root.left)
        right_depth = 1 + self.treeDepth(root.right)
        return max(left_depth, right_depth)
