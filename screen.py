import pygame
import consts
import random

import game_field

pygame.init()

pygame.display.set_caption("The Flag")
screen = pygame.display.set_mode([900, 500])
background = consts.GREEN

#function to make bushes randints random
def screen_display():
    screen.fill(background)
    for i in range(20):
        bush_y = random.randint(0, 400)
        bush_x = random.randint(0,800)
        screen.blit(consts.BUSH, (bush_x, bush_y))
    pygame.display.update()


def draw_grid():
    screen.fill(consts.BLACK)
    for x in range(consts.WINDOW_WIDTH):
        for y in range(consts.WINDOW_HEIGHT):
            rect = pygame.Rect(x * consts.GRID_SIZE, y * consts.GRID_SIZE, consts.GRID_SIZE, consts.GRID_SIZE)
            pygame.draw.rect(screen, consts.GREEN, rect, 1)
    game_field.mine_placement()
    pygame.display.flip()
