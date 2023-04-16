import heapq

from Location import Location
from Map import Map


class other:
    @staticmethod
    def heuristic(node1, node2):
        return abs(node1.x - node2.y) + abs(node1.x - node2.y)

    # Define the Jump Point Search algorithm
    def jump_point_search(self, start: Location, goal: Location, matrix: Map):
        # Define the directions of movement
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        # Define the nodes to be explored
        open_list = [(self.heuristic(start, goal), start)]
        heapq.heapify(open_list)

        # Define the nodes that have already been explored
        closed_list = set()

        # Define the parent of each node in the shortest path
        parents = dict()

        # Define the cost of the shortest path to each node
        g_scores = {start: 0}

        while open_list:
            current = heapq.heappop(open_list)[1]

            # If the current node is the goal, we have found the shortest path
            if current == goal:
                path = []
                while current in parents:
                    path.append(current)
                    current = parents[current]
                path.append(start)
                path.reverse()
                return path

            closed_list.add(current)

            # For each direction of movement
            for direction in directions:
                next_node = Location(current.x + direction[0], current.y + direction[1])

                # If the next node is outside of the matrix, skip it
                if next_node.x < 0 or next_node.x >= matrix.width or next_node.y < 0 or next_node.y >= matrix.height:
                    continue

                # If the next node is an obstacle, skip it
                if matrix.matrix[next_node.x][next_node.y] == "*":
                    continue

                # Calculate the cost of reaching the next node
                cost = g_scores[current] + 1

                # If the next node has already been explored and the new cost is higher, skip it
                if next_node in closed_list and cost >= g_scores.get(next_node, float('inf')):
                    continue

                # If the next node has not yet been explored, or the new cost is lower
                if cost < g_scores.get(next_node, float('inf')):
                    g_scores[next_node] = cost
                    priority = cost + self.heuristic(next_node, goal)
                    heapq.heappush(open_list, (priority, next_node))
                    parents[next_node] = current

        # If we have explored all possible paths and have not found the goal, there is no path
        return None

    # Run the algorithm with the given start and goal nodes
