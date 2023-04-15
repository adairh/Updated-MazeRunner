# import heapq
#
#
# class JPS:
#
#     def __init__(self, map):
#         self.map = map
#         self.start = (map.bot.loc.x, map.bot.loc.y)
#         self.goal = (map.coin.loc.x, map.coin.loc.y)
#         self.matrix = map.matrix
#
#     @staticmethod
#     def heuristic(node1, node2):
#         return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])
#
#     def jump_point_search(self):
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
#         open_list = [(self.heuristic(self.start, self.goal), self.start)]
#         heapq.heapify(open_list)
#
#         closed_list = set()
#
#         parents = dict()
#
#         g_scores = {(self.start[0], self.start[1]): 0}
#
#         while open_list:
#             current = heapq.heappop(open_list)[1]
#
#             if current == self.goal:
#                 path = []
#                 while current in parents:
#                     path.append(current)
#                     current = parents[current]
#                 path.append(self.start)
#                 path.reverse()
#                 return path
#
#             closed_list.add(current)
#
#             for direction in directions:
#                 next_node = (current[0] + direction[0], current[0] + direction[1])
#
#                 if next_node[0] < 0 or next_node[0] >= len(self.matrix) or next_node[1] < 0 or next_node[1] >= len(
#                         self.matrix[0]):
#                     continue
#
#                 if self.matrix[next_node[0]][next_node[1]] == "*":
#                     continue
#
#                 cost = g_scores[current] + 1
#
#                 if next_node in closed_list and cost >= g_scores.get(next_node, float('inf')):
#                     continue
#
#                 if cost < g_scores.get(next_node, float('inf')):
#                     g_scores[next_node] = cost
#                     priority = cost + self.heuristic(next_node, self.goal)
#                     heapq.heappush(open_list, (priority, next_node))
#                     parents[next_node] = current
#
#         return None

