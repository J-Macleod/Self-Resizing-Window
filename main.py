# Self Resizing Window
# by Jacob Macleod
# Started in 2020
# Updated in 2022

import pygame
import os

global x
global y

x = 1000
y = 580

xint = int(x)
yint = int(y)

pygame.init()

icon = pygame.image.load("images/icon.png")

display_width = xint
display_height = yint
fps = 75

os.environ['SDL_VIDEO_CENTERED'] = "1"

pygame.display.set_icon(icon)
pygame.display.set_caption("Self Resizing Window")
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

def change_screen(counterx, countery):
    gameDisplay = pygame.display.set_mode((display_width + counterx, display_height + countery))

def main():

    start = True

    counterx = 0
    countery = 0

    going = "in"

    while start:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill((0, 0, 0))

        if going == "out":
            if counterx == 0:
                going = "in"
            else:
                counterx += 1
                countery += 1

        if going == "in":
            if countery == -530:
                going = "out"
            else:
                counterx -= 1
                countery -= 1
                
        change_screen(counterx, countery)
            
        pygame.display.update()
        clock.tick(fps)

main()
