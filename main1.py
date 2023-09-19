import pygame
import screen
import consts

running = True
screen.screen_display()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.draw_grid()
    pygame.display.flip()
    pass
