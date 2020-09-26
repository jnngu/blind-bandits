import random

class Board:
    def __init__(self, xdim, ydim):
        self.grid = [[0 for x in range(xdim)] for y in range(ydim)]

    

invalidPos = True

while invalidPos:
    player_pos = (random.choice(range(0, 6)), random.choice(range(0, 6)))
    if grid

