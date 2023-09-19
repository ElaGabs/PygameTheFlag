import pygame
import consts
pygame.init()

screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("The Flag")

background_color = consts.GREEN

bush = pygame.image.load("grass.png")




# we use the sizes to draw as well as to do our "steps" in the loops.
grid_node_width = 10
grid_node_height = 10

def createSquare(x, y, color):
    pygame.draw.rect(gridDisplay, color, [x, y, grid_node_width, grid_node_height ])

def visualizeGrid():
    y = 0  # we start at the top of the screen
    for row in matrix:
        x = 0 # for every row we start at the left of the screen again
        for item in row:
            if item == 0:
                createSquare(x, y, (255, 255, 255))
            else:
                createSquare(x, y, (0, 0, 0))

            x += grid_node_width # for ever item/number in that row we move one "step" to the right
        y += grid_node_height   # for every new row we move one "step" downwards
    pygame.display.update()


visualizeGrid()  # call the function
while True:
    pass  # keeps the window open so you can see the result.