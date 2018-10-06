# Author: cym

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        que = [root]
        ans = 0
        while len(que):
            node = que[0]
            que = que[1:]
            if node.left is not None:
                if node.left.left is None and node.left.right is None:
                    ans += node.left.val
                else:
                    que.append(node.left)
            if node.right is not None:
                que.append(node.right)
        return ans

      


