

import numpy
serial = 1723

def power(x, y):
    rack = (x + 1) + 10
    power = rack * (y + 1)
    power += serial
    power *= rack
    return (power // 100 % 10) - 5

def calculate_power_level(x, y):
    rack_id = (x + 1) + 10
    power_level = rack_id * (y + 1)
    power_level += serial
    power_level *= rack_id
    return ((power_level // 100)%10) - 5

grid = numpy.fromfunction(calculate_power_level, (300, 300))

max_power = 0
max_location = None
max_width = 0

for width in range(3, 300):
    windows = sum(grid[x:x-width+1 or None, y:y-width+1 or None] for x in range(width) for y in range(width))
    maximum = int(windows.max())
    location = numpy.where(windows == maximum)

    print(width, maximum, location[0][0] + 1, location[1][0] + 1, max_power)

    if maximum > max_power:
        max_power = maximum
        max_location = numpy.where(windows == maximum)
        max_width = width

print(max_width, max_power, max_location[0][0] + 1, max_location[1][0] + 1)