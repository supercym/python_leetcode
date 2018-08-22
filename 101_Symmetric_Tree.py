# Author: cym

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # *********    recursive    *************
        # if root is None:
        #     return True
        # return self.sym(root.left, root.right)

    # def sym(self, left, right):
    #     if left is None and right is None:
    #         return True
    #     if left and right and left.val == right.val:
    #         return self.sym(left.left, right.right) and self.sym(left.right, right.left)
    #     return False

        # *********    iterative    *************
        if root is None:
            return True
        if root.left is None and root.right is not None:
            return False
        if root.left is not None and root.right is None:
            return False
        if root.left is None and root.right is None:
            return True

        stack1 = []
        stack2 = []
        stack1.append(root.left)
        stack2.append(root.right)
        while len(stack1) != 0 and len(stack2) != 0:
            n1 = stack1.pop()
            n2 = stack2.pop()

            if n1.val != n2.val:
                return False


            if n1.left is None and n2.right is not None:
                return False
            if n1.left is not None and n2.right is None:
                return False
            if n1.right is None and n2.left is not None:
                return False
            if n1.right is not None and n2.left is None:
                return False

            if n1.left and n2.right:
                stack1.append(n1.left)
                stack2.append(n2.right)
            if n1.right and n2.left:
                stack1.append(n1.right)
                stack2.append(n2.left)
        return True





