import heapq
import math

def dijkstra(matrix, start):
    m, n = len(matrix), len(matrix[0])
    distances = [[math.inf for _ in range(n)] for _ in range(m)]
    distances[start[0]][start[1]] = 0
    pq = [(0, start)]
    while pq:
        (curr_dist, (curr_row, curr_col)) = heapq.heappop(pq)
        if curr_dist > distances[curr_row][curr_col]:
            continue
        for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r, c = curr_row + dr, curr_col + dc
            if 0 <= r < m and 0 <= c < n and matrix[r][c] != '*':
                weight = 1
                distance = curr_dist + weight
                if distance < distances[r][c]:
                    distances[r][c] = distance
                    heapq.heappush(pq, (distance, (r, c)))
    return distances

matrix = [
    [" ", " ", "*", "*", " "],
    ["*", " ", "*", " ", " "],
    ["*", " ", "*", " ", "*"],
    ["*", " ", "*", " ", "*"],
    ["*", " ", " ", " ", "*"],
    ["*", "*", " ", " ", "*"],
    ["*", " ", " ", " ", "*"],
    ["*", " ", " ", " ", "*"],
    ["*", " ", " ", " ", "*"],
    ["*", " ", " ", " ", "*"],
    ["*", " ", "*", "*", "*"],
    ["*", " ", " ", " ", "*"],
    ["*", " ", "*", " ", " "],
    [" ", " ", "*", "*", " "]
]

med = 0
for i in [(0, 0), (0, 4), (13, 0), (13, 4)]:
    distances = dijkstra(matrix, i)
    smed = 0
    csmed = 0
    for row in distances:
        for col in row:
            if not math.isinf(col):
                csmed += 1
                smed += col
        print(row)
    print("")
    med += (smed/csmed)
print(med/4)
