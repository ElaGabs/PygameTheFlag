import pygame
import consts
import random
pygame.init()

pygame.display.set_caption("The Flag")
screen = pygame.display.set_mode([900, 500])
background = consts.GREEN


#function to make bushes randints random
def bush_placement():
    for i in range(20):
        bush_y = random.randint(0, 400)
        bush_x = random.randint(0,400)
        screen.blit(consts.BUSH, (bush_x, bush_y))
    pygame.display.update()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background)
    bush_placement()
    pygame.display.flip()
    pass



