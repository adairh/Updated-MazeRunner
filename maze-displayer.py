import json
import pygame
import pygame.font

# Screen dimensions
x_offset = 50
y_offset = 5
SCREEN_WIDTH = 800 - y_offset
SCREEN_HEIGHT = 800 - x_offset

# Initialize pygame and create screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Maze Game')

# Load maze data from file
with open('maze_metadata.json', 'r') as f:
    maze_data = json.load(f)

    # Calculate cell dimensions based on maze size and screen dimensions
    cell_width = SCREEN_WIDTH // maze_data['width']
    cell_height = SCREEN_HEIGHT // maze_data['height']

    # Load and scale images
    bot_img = pygame.transform.scale(pygame.image.load(r'assets\superhero.png'), (cell_width, cell_height))
    coin_img = pygame.transform.scale(pygame.image.load(r'assets\coin.png'), (cell_width, cell_height))
    tree_img = pygame.transform.scale(pygame.image.load(r'assets\apple-tree.png'), (cell_width, cell_height))
    background_img = pygame.transform.scale(pygame.image.load(r'assets\cobble.png'), (cell_width, cell_height))

listOfScore = []
def show_score():
    font = pygame.font.SysFont('Cucho', 24)
    score = font.render("SCORE: " + str(listOfScore), True, (128, 0, 0))

    pygame.draw.rect(screen, (1, 239, 213), (0, 0, 800, x_offset - 10))
    screen.blit(score, (30, (x_offset - 10)//2))
    pygame.display.update()

def draw():
    for i in range(maze_data['height']):
        for j in range(maze_data['width']):
            y = j * cell_width
            x = i * cell_height
            screen.blit(background_img, (y + y_offset, x + x_offset))
            pygame.draw.rect(screen, pygame.Color('black'), pygame.Rect(y + y_offset, x + x_offset, cell_width, cell_height), 1)

    # Draw bots, obstacles, and coin
    for bot in maze_data['bots']:
        if bot['status'] == "eliminated":
            continue
        pos = bot['pos']
        screen.blit(bot_img, (pos[1] * cell_width + y_offset, pos[0] * cell_height + x_offset))
        listOfScore.append(bot['name'] + ": " + str(bot['score']))

    for obs in maze_data['obstacles']:
        screen.blit(tree_img, (obs[1] * cell_width + cell_width // 2 - tree_img.get_width() // 2 + y_offset,
                               obs[0] * cell_height + cell_height // 2 - tree_img.get_height() // 2 + x_offset))

    coin_pos = maze_data['coin']
    screen.blit(coin_img, (coin_pos[1] * cell_width + cell_width // 2 - coin_img.get_width() // 2 + y_offset,
                           coin_pos[0] * cell_height + cell_height // 2 - coin_img.get_height() // 2 + x_offset))


draw()
show_score()
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background and grid lines
    # Update screen
    pygame.display.flip()
    # If screen needs to be hidden, update maze data and rewrite file
    try:
        with open('maze_metadata.json', 'r+') as f:
            temp = json.load(f)
            if not temp['screen']:
                print(temp['screen'])
                maze_data = temp
                maze_data['screen'] = True
                print(maze_data)
                f.seek(0)
                json.dump(maze_data, f)
                f.truncate()
                draw()
                show_score()
    except (FileNotFoundError, json.JSONDecodeError):
        pass




# Quit pygame
pygame.quit()
