# Author: cym

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def binaryTreePaths(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[str]
    #     """
    #     def preOrder(root, path, ans):
    #         if root.left is None and root.right is None:
    #             ans.append(path + str(root.val))
    #             return
    #         if root.left:
    #             preOrder(root.left, path + str(root.val) + '->', ans)
    #         if root.right:
    #             preOrder(root.right, path + str(root.val) + '->', ans)
    #     if root is None:
    #         return []
    #     path =  ""
    #     ans = []
    #     preOrder(root, path, ans)
    #     return ans

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        if root is None:
            return []
        path =  ""
        ans = []
        self.preOrder(root, path, ans)
        return ans

    def preOrder(self, root, path, ans):
            if root.left is None and root.right is None:
                ans.append(path + str(root.val))
                return
            if root.left:
                self.preOrder(root.left, path + str(root.val) + '->', ans)
            if root.right:
                self.preOrder(root.right, path + str(root.val) + '->', ans)
