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
    def __init__(self, maze_file: str):
        self.maze_file = maze_file
        self.last_modified = None

    def run(self):
        time.sleep(5)
        try:
            # check if the file has been modified
            self.last_modified = os.path.getmtime(self.maze_file)
            with open(self.maze_file, 'r') as file:
                data = json.load(file)
                m = Map(data)
                bot = Bot(m, data).getBot("songoku")
                m.addBot(bot)
                if bot.getStatus() == "move":
                    print("move")
                    start = datetime.datetime.now()
                    path = AStarFinder().find_path(m, bot)
                    path.remove(path[0])
                    print(path)
                    choose = path[0]
                    end = datetime.datetime.now()
                    step = self.location_translator(choose, bot.loc)
                    res = bot.doMove(step)
                    print(res)
                    if res:
                        bot.setStatus("stop")
                        data = bot.update()
                        with open(self.maze_file, 'w') as f:
                            json.dump(data, f)
                            time_elapsed = (end - start).microseconds / 1000
                            bot.write(f"{step} {time_elapsed:.2f}")
                    del path, choose, step, res, f
                del data, m, bot
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # continue with the next iteration of the loop

    @staticmethod
    def location_translator(new: Location, old: Location) -> List[str]:
        print([old, new])
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
