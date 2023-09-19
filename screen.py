import pygame
import consts
import random
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


