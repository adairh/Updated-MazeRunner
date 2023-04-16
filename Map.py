import heapq
import math
from typing import List

from Bot import Bot
from Coin import Coin
from Location import Location


class Map:
    width: int = None
    height: int = None
    matrix = None
    obstacles: List[Location] = None
    coin: Coin = None
    locations = None
    bot = []

    def __init__(self, data):
        # self.outputFile = outputF
        # self.inputFile = inputF
        self.data = data
        self.loadJson()
        self.loadLocs()
        self.loadMap()
        # self.printMap()
        # print(self.findCenter())

    def loadJson(self):
        #with open(self.inputFile, 'r') as file:
        self.width = self.data['width']
        self.height = self.data['height']
        self.matrix = [[0] * self.height] * self.width
        self.obstacles: List[Location] = [Location(*loc)
                                          for loc in sorted(self.data['obstacles'], key=lambda x: (x[0], x[1]))]
        self.coin = Coin(Location(*self.data['coin']), self.height, self.width)

    def loadLocs(self):
        self.locations = self.obstacles.copy()
        self.locations.append(self.coin.loc)

    def placeCoin(self):
        coin = self.coin
        self.matrix[coin.loc.x][coin.loc.y] = 'o'

    def loadMap(self):
        self.matrix = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for ll in self.obstacles:
            self.matrix[ll.x][ll.y] = '*'
        self.placeCoin()

    def loadBot(self):
        for bot in self.data['bots']:
            self.bot.append(Bot(self, self.data).getBot(bot["name"]))

    def addBot(self, bot: Bot):
        self.bot.append(bot)
        self.matrix[bot.loc.x][bot.loc.y] = 'X'

    def printMap(self):
        print('*' * (self.width + 2))
        for i in range(self.height):
            print('*', end='')
            for j in range(self.width):
                print('{}'.format(self.matrix[i][j]), end='')
            print('*', end='')
            print()
        print('*' * (self.width + 2))
    def dijkstra(self, temp, start):
        m, n = self.height, self.width
        distances = [[math.inf for _ in range(n)] for _ in range(m)]
        distances[start[0]][start[1]] = 0
        pq = [(0, start)]
        while pq:
            (curr_dist, (curr_row, curr_col)) = heapq.heappop(pq)
            if curr_dist > distances[curr_row][curr_col]:
                continue
            for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, c = curr_row + dr, curr_col + dc
                if 0 <= r < m and 0 <= c < n and temp[r][c] != '*':
                    weight = 1
                    distance = curr_dist + weight
                    if distance < distances[r][c]:
                        distances[r][c] = distance
                        heapq.heappush(pq, (distance, (r, c)))
        return distances

    def findCenter(self):
        med = 0
        for i in [[0, 0], [0, self.width-1], [self.height-1, 0], [self.height-1, self.width-1]]:
            temp = self.matrix
            for a in range(2):
                for b in range(2):
                    x, y = i[0] + a, i[1] + b
                    if 0 < x < self.height and 0 < y < self.width:
                        temp[x][y] = " "

            distances = self.dijkstra(temp, i)
            smed = 0
            csmed = 0
            for row in distances:
                for col in row:
                    if not math.isinf(col):
                        csmed += 1
                        smed += col
                    print(row)
                print("")
            med += (smed / csmed)
        print(med)
        med = (med/4)//1
        q = 0
        w = 0
        for row in distances:
            for col in row:
                if col == med:
                    return [q, w]
                w += 1
            q += 1

