import json
import random

from Location import Location


class Coin:
    def __init__(self, coin: Location, height, width):
        self.loc: Location = coin
        self.x_range = [0, height-1]
        self.y_range = [0, width-1]
        # self.create_coins()

    # def create_coins(self):
    #     while len(self.positions) < self.x_range[1] * self.y_range[1]:
    #         x, y = self.generate_random_position()
    #         self.positions.add((x, y))

    def generate_random_position(self, avoiding):
        while True:
            # Random x, y position for the coin
            x = random.randint(self.x_range[0], self.x_range[1])
            y = random.randint(self.y_range[0], self.y_range[1])

            # Check if the coin is not on an obstacle
            if Location(x, y) not in avoiding:
                return x, y

    def store_new_coin(self, inputFile, avoiding):
        with open(inputFile, 'r') as f:
            data = json.load(f)
        self.loc.x, self.loc.y = self.generate_random_position(avoiding)
        data['coin'] = [self.loc.x, self.loc.y]
        with open(inputFile, 'w') as f:
            json.dump(data, f)
        return self.loc.x, self.loc.y


#
# # Define the main function
# def main():
#     # Set up the game parameters
#     x_range = (0, 10)
#     y_range = (0, 10)
#     obstacles = [(2, 2), (3, 5), (7, 8)]
#     bot_position = (5, 5)
#
#     # Create a Coin object and print its positions
#     coins = Coin(x_range, y_range, obstacles, bot_position)
#     print(coins)
#
#
# # Call the main function
# if __name__ == "__main__":
#     main()
