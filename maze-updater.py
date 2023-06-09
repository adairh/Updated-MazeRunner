import argparse
import json
import os
import random
import time


def parse_arguments():
    parser = argparse.ArgumentParser(description='Maze updater')
    parser.add_argument('-i', '--input', nargs='+', required=True, help='Input files')
    parser.add_argument('-o', '--output', required=True, help='Output file')
    return parser.parse_args()


def read_json_file(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)


def write_json_file(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file)



def get_latest_input_lines(input_files):
    lines = []
    for file_name in input_files:
        eachFile = []
        with open(file_name, 'r') as file:
            for line in file.readlines():
                line = line.strip()
                if line:
                    eachFile.append([file_name.replace(".txt", ""), *line.split(' ')])
        if len(eachFile) > 0:
            lines.append(eachFile[-1])
    return sorted(lines, key=lambda xx: float(xx[2]))


def move_bot(bot, direction, occupied_slots):
    x, y = bot["pos"]
    offset = {"right": (0, 1), "left": (0, -1), "down": (1, 0), "up": (-1, 0)}[direction]
    x_off, y_off = offset
    new_pos = (x + x_off, y + y_off)
    if new_pos not in occupied_slots:
        bot["pos"] = new_pos
        bot["status"] = "move"
        return True
    else:
        bot["status"] = "eliminated"
        return False


def get_occupied_slots(bots):
    return {tuple(bot["pos"]) for bot in bots}


args = parse_arguments()
input_files = args.input
output_file = args.output

def generate_random_position(w, h, avoiding):
    while True:
        # Random x, y position for the coin
        x = random.randint(0, h - 1)
        y = random.randint(0, w - 1)

        # Check if the coin is not on an obstacle
        if [x, y] not in avoiding:
            return x, y


while True:
    time.sleep(0.1)
    # Wait for input files to have content
    while not any(os.stat(file_name).st_size != 0 for file_name in input_files):
        time.sleep(0.1)

    # Read input files and sort by time
    input_lines = get_latest_input_lines(input_files)
    print(input_lines)
    # Load maze metadata
    while True:
        try:
            data = read_json_file("maze_metadata.json")
            break
        except ValueError:
            pass
        except FileNotFoundError:
            print(f"Error: maze_metadata.json not found")
            exit()

    # Check if any bot can move
    alive = True
    obss = []
    if not any(bot["status"] == "move" for bot in data["bots"]):
        print("")
        for item in input_lines:
            bot = next((bot for bot in data["bots"] if bot["name"] == item[0]), None)
            obss.append(bot['pos'])
            if bot:
                occupied_slots = get_occupied_slots(data["bots"])
                alive = move_bot(bot, item[1], occupied_slots)
                print("Move bot: " + str(bot) + " " + str(item))
                occupied_slots = get_occupied_slots(data["bots"])

    for bot in data['bots']:
        if bot['pos'] == data['coin']:
            bot['score'] += 1
            obss = obss + data['obstacles']
            cx, cy = generate_random_position(data['width'], data['height'], obss)
            data['coin'] = [cx, cy]

    # Update maze metadata
    write_json_file("maze_metadata.json", data)
    if not alive:
        break
exit()
    # Wait for user input
