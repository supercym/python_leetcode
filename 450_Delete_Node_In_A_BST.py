# Author: cym

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val == key:
            left, right = root.left, root.right
            if left is None:
                root = right
            elif right is None:
                root = left
            else:
                minNode = right ## 右子树最小值对应的点
                while right.left:
                    right = right.left
                minNode = right
                ## 右子树最小值对应的点一定没有左孩子，所以可以调用deleteNode()
                minNode.right = self.deleteNode(root.right, minNode.val)
                minNode.left = left
                root = minNode

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

