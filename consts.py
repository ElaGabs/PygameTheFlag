#colors
import pygame

GREEN = (69, 139, 0)
BUSH = pygame.transform.scale(pygame.image.load("grass.png"), (50, 60))

MESSAGE = "Welcome to The Flag game. Have Fun!"
WIN_MSG = ""
LOSE_MSG = ""

FLAG = 1
MINE = 2
SOLIDER = 3

GRID_SIZE = 20
BOARD_GRID_ROWS = 50
BOARD_GRID_COLS = 25
WINDOW_WIDTH = BOARD_GRID_ROWS * GRID_SIZE  # 1000
WINDOW_HEIGHT = BOARD_GRID_COLS * GRID_SIZE  # 500

PLAYER_WIDTH = 2 * GRID_SIZE  # 40
PLAYER_LENGTH = 4 * GRID_SIZE  # 80
FLAG_WIDTH = 4
FLAG_LENGTH = 3
MINE_WIDTH = 3 * GRID_SIZE  # 60
MINE_LENGTH = 1 * GRID_SIZE  # 20

NEW_FLAG_WIDTH = (BOARD_GRID_ROWS - FLAG_WIDTH)  # 46
NEW_FLAG_LENGTH = (BOARD_GRID_COLS - FLAG_LENGTH)  # 22

INJURY_IMG = pygame.image.load("injury.png")
PLAYER_IMG = pygame.image.load("soldier.png")
MINE_IMG = pygame.image.load("mine.png")
GRASS_IMG = pygame.image.load("grass.png")
FLAG_IMG = pygame.image.load("flag.png")

MINE_IMG = pygame.transform.scale(MINE_IMG, (MINE_WIDTH, MINE_LENGTH))
FLAG_IMG = pygame.transform.scale(FLAG_IMG, (FLAG_WIDTH * GRID_SIZE, FLAG_LENGTH * GRID_SIZE))
GRASS_IMG = pygame.transform.scale(GRASS_IMG, (50, 50))
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_LENGTH, PLAYER_LENGTH))
INJURY_IMG = pygame.transform.scale(INJURY_IMG, (PLAYER_LENGTH, PLAYER_LENGTH))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FIELD_COLOR = (46, 139, 87)
# FONT = pygame.font.SysFont("Arial", 36)


RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3
