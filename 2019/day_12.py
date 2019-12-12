import re

from itertools import combinations

def parse(s):
  m = re.search(r'^<x=(\S+), y=(\S+), z=(\S+)>$', s)
  return [int(x) for x in m.groups()]


def compare(a, b):
  return (a > b) - (a < b)


def get_velocity(moon1, moon2):
    return [compare(moon1[0], moon2[0]), compare(moon1[1], moon2[1]), compare(moon1[2], moon2[2])]


def get_energy(position, velocity):
  return sum(abs(x) for x in position) * sum(abs(x) for x in velocity)


def move(p, v):
  for n in range(len(p)):
    p[n] += v[n]
  return p

program_input = """<x=14, y=15, z=-2>
<x=17, y=-3, z=4>
<x=6, y=12, z=-13>
<x=-2, y=10, z=-8>"""

positions = [parse(x) for x in program_input.split("\n")]
velocities = [[0, 0, 0] for _ in positions]

STEPS = 1000

for _ in range(STEPS):
    for i1, i2 in combinations(range(len(positions)), 2):
        for n, v in enumerate(get_velocity(positions[i1], positions[i2])):
            velocities[i1][n] -= v
            velocities[i2][n] += v

    for i in range(len(positions)):
        positions[i] = move(positions[i], velocities[i])


print("Answer to question 1: ", sum(get_energy(positions[i], velocities[i]) for i in range(len(positions))))