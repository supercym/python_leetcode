# Author: cym

# *************    Dijkstra    *****************
# *************    Low Efficient    *****************
# def minPathSum(grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         m = len(grid)
#         if m == 0:
#             return 0
#         n = len(grid[0])
#         if n == 0:
#             return 0
#         mm, nn = m-1, n-1
#
#         processed = []
#         costs = {}
#         parents = {}
#         for i in range(m):
#             for j in range(n):
#                 costs[(i, j)] = float("inf")
#                 parents[(i, j)] = None
#         costs[(0, 0)] = grid[0][0]
#         node = find_lowest_cost(costs, processed)
#
#         while node is not None:
#             cost = costs[node]
#             node_down_neighbor = (node[0]+1, node[1])
#             node_right_neighbor = (node[0], node[1]+1)
#
#             if node[0] < mm and node[1] < nn:
#                 neighbors = [node_down_neighbor, node_right_neighbor]
#             elif node[0] == mm and node[1] != nn:
#                 neighbors = [node_right_neighbor]
#             elif node[0] != mm and node[1] == nn:
#                 neighbors = [node_down_neighbor]
#             else:
#                 neighbors = []
#
#             for n in neighbors:
#                 new_cost = cost + grid[n[0]][n[1]]
#                 if new_cost < costs[n]:
#                     costs[n] = new_cost
#                     parents[n] = node
#
#             processed.append(node)
#             node = find_lowest_cost(costs, processed)
#
#         return costs[(mm, nn)]
#
#
# def find_lowest_cost(costs, processed):
#     lowest_cost = float("inf")
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node


def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    if m == 0:
        return 0
    n = len(grid[0])
    if n == 0:
        return 0
    for i in range(m):
        for j in range(n):
            if i == 0 and j != 0:
                grid[i][j] += grid[i][j-1]
            elif i != 0 and j == 0:
                grid[i][j] += grid[i-1][j]
            elif i != 0 and j != 0:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[m-1][n-1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(minPathSum(grid))
    grid2 = [[8,6,5,5,9,8,4,3,6,4,5,0,6,4],
             [0,1,9,1,0,6,7,6,5,7,0,6,4,4],
             [3,9,0,3,6,5,8,5,3,4,0,1,0,5],
             [1,7,1,3,8,3,4,1,9,4,7,4,1,0],
             [1,5,4,6,7,4,1,3,9,9,0,4,5,0],
             [8,6,7,9,5,1,5,5,4,1,6,5,5,6],
             [1,8,6,4,6,2,0,3,8,1,8,9,2,0],
             [5,0,0,3,8,9,5,3,2,0,8,6,3,7],
             [1,1,3,3,9,1,7,5,5,0,0,3,3,0],
             [4,6,0,9,8,2,3,6,4,8,9,6,0,9],
             [3,3,6,6,4,1,9,6,2,9,3,7,9,4],
             [2,2,6,6,0,7,8,8,1,1,4,5,1,5],
             [4,1,7,7,6,3,5,3,5,5,9,9,6,2]]
    print(minPathSum(grid2))

