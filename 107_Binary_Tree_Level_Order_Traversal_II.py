# Author: cym

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        total_level = []

        if root is None:
            return total_level

        processed = []
        processed.append(root)
        while len(processed) != 0:
            tmp = []
            level = []
            while len(processed) != 0:
                node = processed[0]
                processed = processed[1:]

                level.append(node.val)

                if node.left is not None:
                    tmp.append(node.left)
                if node.right is not None:
                    tmp.append(node.right)
            total_level.append(level)
            processed = tmp

        return total_level[::-1]
