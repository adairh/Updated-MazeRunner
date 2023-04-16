import string

import Map
from Location import Location


class Bot:
    loc: Location
    map: Map
    botName: string = ""
    outputFile = ""
    touchingOutput = True
    score = -1
    status = ""

    def __init__(self, m: Map, data):
        self.data = data
        self.map = m

    def getOccupiedSlot(self):
        oc = []
        for b in self.data["bots"]:
            if b["name"] != self.botName:
                oc.append(Location(*b["pos"]))
        return oc

    def setStatus(self, status):
        for bot in self.data['bots']:
            if bot["name"] == self.botName:
                self.status = status

    def getStatus(self):
        for bot in self.data['bots']:
            if bot["name"] == self.botName:
                return self.status

    def getBot(self, name):
        for bot in self.data['bots']:
            if bot['name'] == name:
                self.loc = Location(*bot['pos'])
                self.botName = bot["name"]
                self.score = bot["score"]
                self.status = bot["status"]
                self.outputFile = name + ".txt"
                return self
        return None

    def update(self):
        for bot in self.data['bots']:
            if bot['name'] == self.botName:
                bot['pos'] = [self.loc.x, self.loc.y]
                bot["name"] = self.botName
                bot["score"] = self.score
                bot["status"] = self.status
        return self.data

    def moveBot(self, loc: Location):

        if loc not in self.map.obstacles and loc not in self.getOccupiedSlot():
            if loc == self.map.coin.loc:
                self.score += 1
                botLoc = [loc]
                botLoc = botLoc + self.getOccupiedSlot()
                self.map.coin.loc.x, self.map.coin.loc.y = self.map.coin.generate_random_position(
                    self.map.obstacles + botLoc)
                # sound.maze_sound().sound_ate()
            # self.loc = loc
            # self.printMap()
            return True
        else:
            return False
            # self.loadMap()

    def moveTo(self, loc: Location):
        tx = loc.x - self.loc.x
        ty = loc.y - self.loc.y

        flagA = True
        flagB = True
        if tx < 0:
            tx = -tx
            for i in range(tx):
                if not self.up():
                    flagA = False
                else:
                    flagA = True
        else:
            for i in range(tx):
                if not self.down():
                    flagA = False
                else:
                    flagA = True
        if ty < 0:
            ty = -ty
            for i in range(ty):
                if not self.left():
                    flagB = False
                else:
                    flagB = True
        else:
            for i in range(ty):
                if not self.right():
                    flagB = False
                else:
                    flagB = True

        if not flagA and not flagB:
            return False
        return True

    def left(self):
        if self.loc.y > 0:
            return self.moveBot(Location(self.loc.x, self.loc.y - 1))

    def right(self):
        if self.loc.y < self.map.height - 1:
            return self.moveBot(Location(self.loc.x, self.loc.y + 1))

    def up(self):
        if self.loc.x > 0:
            return self.moveBot(Location(self.loc.x - 1, self.loc.y))

    def down(self):
        if self.loc.x < self.map.width - 1:
            return self.moveBot(Location(self.loc.x + 1, self.loc.y))

    def write(self, a):
        with open(self.outputFile, mode='a') as file:
            file.write(a + '\n')

    def doMove(self, step):
        if step == 'up':
            return self.up()
        elif step == 'down':
            return self.down()
        elif step == 'left':
            return self.left()
        elif step == 'right':
            return self.right()
        #print("INVALID STEP: " + str(step))
        return False
