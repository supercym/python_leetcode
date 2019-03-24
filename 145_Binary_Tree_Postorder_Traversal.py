# Author: cym

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if root is None:
            return ans
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack[-1]
            stack = stack[:len(stack)-1]
            ans.append(node.val)

            if node.left is not None:
                stack.append(node.left)

            if node.right is not None:
                stack.append(node.right)

        ans = ans[::-1]
        return ans
