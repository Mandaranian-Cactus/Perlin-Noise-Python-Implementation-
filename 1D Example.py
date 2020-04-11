import pygame
import sys
from Perlin_Noise import Noise
import random

class Window:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode((self.w, self.h))

    def fill(self):
        self.screen.fill((255, 255, 255))


screen = Window(1000, 525)
pygame.init()
clock = pygame.time.Clock()
start = 10000000000
while True:
    screen.fill()

    # Check inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Draw the perlin noise
    temp_start = start
    increment = 0.11232
    x_pos = 0
    n = Noise(temp_start, 0.13)
    prev = n.return_val()
    for i in range(200):
        temp_start += increment
        x_pos += 5
        n = Noise(temp_start, 0.13)
        val = n.return_val()
        pygame.draw.aaline(screen.screen, (0,0,0), (x_pos - 5, prev * 100 + 150), (x_pos, val * 100 + 150))
        prev = val
    start += .11232

    # Draw the random Noise
    prev = random.randrange(-30,31)
    increment = 0.134324
    x_pos = 0
    for i in range(200):
        x_pos += 5
        val = random.randrange(-30, 31)
        pygame.draw.aaline(screen.screen, (0,0,0), (x_pos - 5, prev + 350), (x_pos, val + 350))
        prev = val

    pygame.display.update()
    clock.tick(70)  # Fps (Don't know why/how it does it)