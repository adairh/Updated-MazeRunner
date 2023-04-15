import math


class Location:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Location):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def distance(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

    def getNearby(self):
        res = []
        offset = [[-1, -1], [-1, 0], [-1, 1],
                  [0, -1], [0, 1],
                  [1, -1], [1, 0], [1, 1]]
        for x, y in offset:
            res.append(Location(self.x + x, self.y + y))
        return res
