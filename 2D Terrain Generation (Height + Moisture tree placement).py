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
    max_value = 0   # Used to help the output be within a given range (Range is chosen based on the input data. If the range of input were from -1 to 1, this variable helps mataining that same rangeat output)
    for i in range(octaves):
        persistence = persistences[i]  # Persistence regulates how much an octave affects the final overall outcome
        frequency = frequencies[i]  # Frequency dictates the gap between points on an octave (Smaller gaps have smoother curves while larger gaps have more rigid curves)
        n = Noise(x * frequency, y * frequency)
        total += n.return_val() * persistence
        max_value += persistence
    return total / max_value  # "max_value" is used to keep within input range


screen = Window(800, 575)
pygame.init()
clock = pygame.time.Clock()

w, h = 160, 115
y_pos_set = 100.01

height_map = [[0 for i in range(w)] for i in range(h)]
moisture_map = [[0 for i in range(w)] for i in range(h)]

# Height Map
persistences = [10, 2, 1, 3]
frequencies = [0.5, 2, 1, 0.5]
noise_move_increment = 0.085317
y_pos = 100.01
for i in range(h):
    x_pos = 59.01
    for j in range(w):
        output = add_octaves(x_pos, y_pos, len(persistences), persistences, frequencies)
        output = (output + 1) / 2  # Set within the range from 0 - 2
        output = output ** 2  # Exponential add (This adjusts the range of the output from 0 - 2 to 0 - 2 ** expoenent)
        height_map[i][j] = output
        x_pos += noise_move_increment
    y_pos += noise_move_increment

print("Done Height Map")

# Moisture map
noise_move_increment = 0.025317
persistences = [1, 2, 4, 8, 16]
frequencies = [1, 2, 4, 8, 20]
y_pos = 76.01
for i in range(h):
    x_pos = 26.01
    for j in range(w):
        output = add_octaves(x_pos, y_pos, len(persistences), persistences,frequencies)
        output = (output + 1) / 2  # Set within the range from 0 - 2
        # output = output ** 2  # Exponential add (This adjusts the range of the output from 0 - 2 to 0 - 2 ** expoenent)
        moisture_map[i][j] = output
        x_pos += noise_move_increment
    y_pos += noise_move_increment

print("Done Moisture Map")

# Draw map (Including trees)
screen.fill()
for yc in range(h):
    for xc in range(w):
        height = height_map[yc][xc]
        moisture = moisture_map[yc][xc]

        # Limits for each terrain type (Water, Mountain, forest, etc.)
        if height < 0.1:
            color = (0, 0, 175)  # Water
        elif height < 0.12:
            color = (194, 178, 128)  # Beach
        elif height < 0.25:
            color = (34,139,34)  # Grass
            r = 4  # Less trees
        elif height < 0.35:
            color = (0, 100, 0)  # Forest
            r = 1  # More trees
        elif height < 0.5:
            color = (211, 211, 211)  # Mountain
        else:
            color = (255, 255, 255)  # Snow
        pygame.draw.rect(screen.screen, color, (xc * 5,yc * 5, 5, 5))

        # Tree placement (Naive Solution)
        # Here we check a given point's surroundings to see if that point has the highest value within a radius
        # If so, we place a tree there
        if 0.12 < height < 0.35:
            max_val = moisture_map[yc][xc]
            flag = True  # False means that a neighbor has a higher value
            for yn in range(yc - r, yc + r + 1):
                for xn in range(xc - r, xc + r + 1):
                    if 0 <= xn and xn < w and 0 <= yn and yn < h:
                        val = moisture_map[yn][xn]
                        if val > max_val:
                            flag = False
                            break
                if not flag:
                    break

            if flag:
                pygame.draw.rect(screen.screen, (0,0,0), (xc * 5 + 1, yc * 5 + 1, 5, 5))

pygame.display.update()

while True:
    # Check inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(50)  # Fps (Don't know why/how it does it)