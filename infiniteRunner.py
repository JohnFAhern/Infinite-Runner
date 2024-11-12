import random
import pygame

pygame.init()

#game constants
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

WIDTH = 450
HEIGHT = 300

#game variables
score = 0
player_x = 50
player_y = 200


screen = pygame.display.set_mode({WIDTH, HEIGHT})
pygame.display.set_caption('Infiinite Runner')
background = black
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.clock()

running = True
while running:
        timer.tick(fps)
        screen.fill(background)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
        pygame.display.flip()
pygame.quit()
