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


screen = Window(700, 525)
pygame.init()
clock = pygame.time.Clock()
noise_move_increment = 0.025317
persistences = [1, 0.5, 0.25]
frequencies = [0.5, 1, 2]

w, h = 700, 300
# y_pos_set = 100.1

screen.fill()
y_pos = 100.1
for y in range(h):
    x_pos = 59.01

    for x in range(w):

        output = add_octaves(x_pos, y_pos, len(frequencies),persistences, frequencies)
        output = (output + 1) / 2  # Change range from 0 - 1
        color = output * 255
        screen.screen.set_at((x, y), (color, color, color))
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

