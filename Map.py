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
