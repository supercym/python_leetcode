# Author: cym

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if len(grid) == 0:
            return Node(None, True, None, None, None, None)
        root = Node(None, False, None, None, None, None)
        n = len(grid)
        topLeftSquare, topRightSquare, bottomLeftSquare, bottomRightSquare = [], [], [], []

        testSet1 = set()
        testSet2 = set()
        testSet3 = set()
        testSet4 = set()
        for i in range(int(n/2)):
            topLeftSquare.append(grid[i][:int(n/2)])
            topRightSquare.append(grid[i][int(n/2):])
            testSet1.update(set(grid[i][:int(n/2)]))
            testSet2.update(set(grid[i][int(n/2):]))

        for i in range(int(n/2), n):
            bottomLeftSquare.append(grid[i][:int(n/2)])
            bottomRightSquare.append(grid[i][int(n/2):])
            testSet3.update(set(grid[i][:int(n/2)]))
            testSet4.update(set(grid[i][int(n/2):]))

        if len(testSet1) == 1 and len(testSet2) == 1 and len(testSet3) == 1 and len(testSet4) == 1:
            if grid[0][0] == grid[0][int(n/2)] and grid[0][0] == grid[int(n/2)][0] and grid[0][0] == grid[int(n/2)][int(n/2)]:
                root.val = grid[0][0]
                root.isLeaf = True
                return root

        if len(testSet1) == 1:
            root.topLeft = Node(bool(grid[0][0]), True, None, None, None, None)
        else:
            root.topLeft = self.construct(topLeftSquare)
        if len(testSet2) == 1:
            root.topRight = Node(bool(grid[0][int(n/2)]), True, None, None, None, None)
        else:
            root.topRight = self.construct(topRightSquare)
        if len(testSet3) == 1:
            root.bottomLeft = Node(bool(grid[int(n/2)][0]), True, None, None, None, None)
        else:
            root.bottomLeft = self.construct(bottomLeftSquare)
        if len(testSet4) == 1:
            root.bottomRight = Node(bool(grid[int(n/2)][int(n/2)]), True, None, None, None, None)
        else:
            root.bottomRight = self.construct(bottomRightSquare)

        return root

