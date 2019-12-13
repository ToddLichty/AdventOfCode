import itertools
from IntCode import *

def read_input(file):
    with open(file) as f:
        lines = f.read()
    
    return str(lines)


def cmp(a, b):
  return (a > b) - (a < b)


def arcade(code, play_free=False):
    codes = [int(x) for x in code.split(',')]
    computer = IntCode(codes)

    tiles = dict()
    outputs = []
    score = 0

    if play_free:
        computer.edit(0, 2)

    while True:
        res = computer.run()

        if res == R_HALT:
            break
        elif res == R_OUTPUT:
            outputs.append(computer.read())

            if len(outputs) == 3:
                x = outputs[0]
                y = outputs[1]
                tile_id = outputs[2]

                if x == -1 and y == 0:
                    score = tile_id
                else:
                    tiles[(x, y)] = tile_id

                if tile_id == 3:
                    paddle = x
                elif tile_id == 4:
                    ball = x

                outputs = []
        elif res == R_INPUT:
            computer.write(cmp(ball, paddle))

    return tiles, score


code = read_input('./2019/data/day_13.in')

tiles, _ = arcade(code)
print("Answer for question 1: ", list(tiles.values()).count(2))

_, score = arcade(code, True)
print("Answer for question 2: ", score)