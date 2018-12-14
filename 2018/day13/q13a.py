from collections import defaultdict
from typing import List, Tuple, Dict

class Cart(object):
    def __init__(self, row, column, direction, inter):
        self.row = row
        self.column = column
        self.direction = direction
        self.inter = inter

track = []
carts = []

# up, right, down, left
DR = [-1, 0, 1, 0]
DC = [0,1,0,-1]

def turn_left(d):
    return (d+3)%4

def turn_right(d):
    return (d+1)%4


def read_input(file):
    global track
    for line in open(file):
        if line:
            track.append([c for c in line])

def print_track():
    global track
    global carts
    for r in range(len(track)):
        for c in range(len(track[r])):
            has_cart = False
            for cart in carts:
                if cart.row == r and cart.column == c:
                    print({0: '^', 1:'>', 2:'v', 3:'<'}[cart.direction], end='')
                    has_cart = True
            if not has_cart:
                print(track[r][c], end='')
        print()

#read the input and create the track
read_input('/home/todd/code/AdventOfCode/2018/data/day13test.txt')

#replace carts from the input with the appropriate tracks
for r in range(len(track)):
    for c in range(len(track[r])):
        if track[r][c] == '^':
            track[r][c] = '|'
            carts.append(Cart(r,c,0,0))
        if track[r][c] == '>':
            track[r][c] = '-'
            carts.append(Cart(r,c,1,0))
        elif track[r][c] == 'v':
            track[r][c] = '|'
            carts.append(Cart(r,c,2,0))
        elif track[r][c] == '<':
            track[r][c] = '-'
            carts.append(Cart(r,c,3,0))

crash_found = False

while not crash_found:
    if len(carts) == 1:
        print('{},{}'.format(carts[0].column, carts[0].row))
        crash_found = True
        break

    carts = sorted(carts, key = lambda x: (x.row, x.column))

    for cart in carts:
        next_row = cart.row + DR[cart.direction]
        next_column = cart.column + DC[cart.direction]

        
        next_track_tile = track[next_row][next_column]

        if next_track_tile == '\\':
            cart.direction = {0:3, 1:2, 2:1, 3:0}[cart.direction]
        elif next_track_tile == '/':
            cart.direction = {0:1, 1:0, 2:3, 3:2}[cart.direction]
        elif next_track_tile == '+':
            if cart.inter == 0:
                cart.direction = turn_left(cart.direction)
            elif cart.inter == 1:
                pass
            elif cart.inter == 2:
                cart.direction = turn_right(cart.direction)
            cart.inter = (cart.inter + 1)%3

        if (next_row,next_column) in [(other.row, other.column) for other in carts]:
            carts = [other for other in carts if (other.row, other.column) not in [(cart.row, cart.column),(next_row,next_column)]]

        cart.row = next_row
        cart.column = next_column
