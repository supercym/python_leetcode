# Author: cym

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans = []
        queue = [root]
        while len(queue):
            queT = []
            ansT = []
            for node in queue:
                for c in node.children:
                    queT.append(c)
                ansT.append(node.val)
            ans.append(ansT)
            queue = queT
        return ans

