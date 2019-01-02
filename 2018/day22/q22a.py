import numpy as np
import enum

class RegionType(enum.Enum): 
    rocky = 0
    wet = 1
    narrow = 2

DEPTH = 8787
TARGET = (10, 725)

class Region(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.erosion = 0
        self.type = -1

        self.calculate_geologic_index()
        self.calculate_erosion()

    def calculate_geologic_index(self):
        global cave

        if self.x == 0 and self.y == 0:
            self.geologic_index = 0
        elif self.x == TARGET[1] and self.y == TARGET[0]:
            self.geologic_index = 0
        elif self.y == 0:
            self.geologic_index = self.x * 16807
        elif self.x == 0:
            self.geologic_index = self.y * 48271
        else:
            self.geologic_index = cave[x-1][y].erosion * cave[x][y-1].erosion

    def calculate_erosion(self):
        global DEPTH
        self.erosion = (self.geologic_index + DEPTH) % 20183
        
        if self.erosion % 3 == 0:
            self.type = RegionType.rocky
        elif self.erosion % 3 == 1:
            self.type = RegionType.wet
        else:
            self.type = RegionType.narrow
    
    def __repr__(self):
        return str(self.y) + ", " + str(self.x) + ' - ' + str(self.type)

cave = np.empty((11, 726), dtype=Region)

risk = 0 

for y in range(0, 726):
    for x in range(0, 11):
        cave[x][y] = Region(x, y)
        risk += int(cave[x][y].type.value)

print(risk)
