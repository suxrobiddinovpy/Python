import pygame
from pygame.locals import *
import random

pygame.init()

width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Car Game")

gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

gameover = False
speed = 2
score = 0

clock = pygame.time.Clock()
fps = 120
running = True
while running:
     clock.tick(fps)

     for event in pygame.event.get():
         if event.type == QUIT:
             running = False

    screen.fill(green)

    pygame.display.update()

pygame.quit()
