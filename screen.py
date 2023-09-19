import pygame
import consts
pygame.init()

pygame.display.set_caption("The Flag")
screen = pygame.display.set_mode([900, 500])
background = consts.GREEN
screen.fill(background)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((background))
    pygame.display.flip()
    pass

