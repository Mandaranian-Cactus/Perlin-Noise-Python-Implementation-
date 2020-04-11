from Perlin_Noise import Noise

import pygame
import sys


class Window:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode((self.w, self.h))

    def fill(self):
        self.screen.fill((255, 255, 255))


def fade(t):  # Fade function to smooth out rigidness
    return 6 * t ** 5-15 * t ** 4+10 * t ** 3

def add_octaves(x, y, octaves, persistences, frequencies):  # Here, octaves/perlin noises are combined together
    total = 0  # Total of the accumulated sums of the octaves
    max_value = 0   # Used to keep the output to be between 0 - 1
    for i in range(octaves):
        persistence = persistences[i]  # Persistence regulates how much an octave affects the final overall outcome
        frequency = frequencies[i]  # Frequency dictates the gap between points on an octave (Smaller gaps have smoother curves while larger gaps have more rigid curves)
        n = Noise(x * frequency, y * frequency)
        total += n.return_val() * persistence
        max_value += persistence
    return total / max_value

def lower(x):
    return -.2 * x ** 1.4 + 0.05

def upper(x):
   return -(x) ** (1/2) + 1


screen = Window(700, 525)
pygame.init()
clock = pygame.time.Clock()
noise_move_increment = 0.025317
persistences = [10, 2, 1, 3]
frequencies = [0.5, 2, 1, 0.5]

w, h = 500, 500

screen.fill()
y_pos = 200.01
for y in range(h):
    x_pos = 100.51
    for x in range(w):
        output = add_octaves(x_pos, y_pos, len(persistences), persistences,frequencies)
        output = (output + 1) /2  # Set within the range from 0 - 2
        output = output ** 2  # Exponential add (This adjusts the range of the output from 0 - 2 to 0 - 2 ** expoenent)
        d = abs(x / w - 1 / 2) + abs(
			y / h - 1 / 2)  # We have two "- 1/2" for making sure that d is within the range of 0 - 1
        output = lower(d) + output * (upper(d) - lower(d))
        # Note the operation is exponential so polar points will be stretched out the most

        if output < 0.1:
            color = (0,0,175)  # Water
        elif output < 0.12:
            color = (194, 178, 128)  # Beach
        elif output < 0.17:
            color = (34,139,34)  # Grass
        elif output < 0.35:
            color = ((0,100,0))  # Forest
        elif output < 0.6:
            color = (211, 211, 211)  # Mountain
        else:
            color = (255, 255, 255)

        screen.screen.set_at((x, y), color)
        x_pos += noise_move_increment
    y_pos += noise_move_increment
    pygame.display.update()

while True:
    # Check inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # pygame.display.update()
    clock.tick(50)  # Fps (Don't know why/how it does it)