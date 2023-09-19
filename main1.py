import pygame
import screen
import consts

running = True
screen.screen_display()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    pass
