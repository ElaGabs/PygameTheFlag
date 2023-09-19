#making the grid
import pygame
import random

import consts
import screen


def grid():
    game_field = []
    empty = "EMPTY"
    for row_index in range(25):
        row = []
        for column in range(50):
            row.append(empty)
        game_field.append(row)
    return game_field

def mine_placement():
    game_field = grid()
    count = 0
    while count < 20:
        row = random.randint(0,24)
        item = random.randint(0,49)
        screen.screen.blit(consts.MINE_IMG, (row, item))
    pygame.display.update()
    return game_field

