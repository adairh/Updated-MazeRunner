import datetime
import json
import os
import time
import timeit
from typing import List

from Astar import AStarFinder
from Bot import Bot
from Location import Location
from Map import Map


class BotRunner:
    path = []

    def __init__(self, maze_file: str):
        self.maze_file = maze_file
        self.last_modified = None

    def in_danger(self, bot: Bot):
        for index in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            loc = Location(bot.loc.x + index[0], bot.loc.y + index[1])
            if loc in bot.getOccupiedSlot():
                return loc
        return None

    def run(self):
        time.sleep(0.1)
        try:
            # check if the file has been modified
            self.last_modified = os.path.getmtime(self.maze_file)
            with open(self.maze_file, 'r') as file:
                data = json.load(file)
                if data['screen']:
                    m = Map(data)
                    bot = Bot(m, data).getBot("top")
                    m.addBot(bot)
                    if bot.getStatus() == "move":
                        start = datetime.datetime.now()
                        danger = self.in_danger(bot)
                        if len(self.path) <= 0 or danger is not None:
                            self.path = AStarFinder().find_path(m, bot, [danger])
                        if self.path[-1] != m.coin.loc:
                            self.path = AStarFinder().find_path(m, bot, [])
                        if self.path[0] != bot.loc:
                            self.path = AStarFinder().find_path(m, bot, [])
                        self.path.remove(self.path[0])
                        if len(self.path) > 0:
                            choose = self.path[0]
                            end = datetime.datetime.now()
                            step = self.location_translator(choose, bot.loc)
                            res = bot.doMove(step)
                            if res:
                                bot.setStatus("stop")
                                data = bot.update()
                                data['coin'] = [m.coin.loc.x, m.coin.loc.y]
                                data['screen'] = False
                                with open(self.maze_file, 'w') as f:
                                    json.dump(data, f)
                                    time_elapsed = (end - start).microseconds / 1000
                                    bot.write(f"{step} {time_elapsed:.2f}")
                            del choose, step, res
                    del data, m, bot
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # continue with the next iteration of the loop

    @staticmethod
    def location_translator(new: Location, old: Location) -> List[str]:
        x, y = new.x - old.x, new.y - old.y
        offset = [[-1, 0], [1, 0], [0, -1], [0, 1], 'up', 'down', 'left', 'right']
        for i in range(4):
            if [x, y] == offset[i]:
                return offset[i + 4]


if __name__ == '__main__':
    runner = BotRunner("maze_metadata.json")
    timer = timeit.Timer(runner.run)
    while True:
        timer.timeit(1)
