# Author: cym
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if root is None:
            return ans
        stack = []
        cur = root
        while cur != None or len(stack) > 0:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            node = stack[-1]
            stack = stack[:len(stack)-1]
            ans.append(node.val)
            cur = node.right
        return ans
