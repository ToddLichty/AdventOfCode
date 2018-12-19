import numpy as np
import copy

OPEN_GROUND = '.'
TREES = '|'
LUMBERYARD = '#'


def read_input(file):
    with open(file) as f:
        lines = f.readlines()
    return [list((x.strip())) for x in lines] 

landscape = np.asarray(read_input('/home/todd/code/AdventOfCode/2018/data/day18.txt'))

for minute in range(1, 1000000001):

    if minute % 1000000 == 0:
        print(minute)
        
    new_landscape = copy.deepcopy(landscape)

    for y in range(len(landscape)):
        for x in range(len(landscape[0])):
            acre = new_landscape[y, x]
            
            x1 = max(x-1,0)
            x2 = min(x+2,len(landscape[0]))
            y1 = max(y-1,0)
            y2 = min(y+2,len(landscape))
            subfield = landscape[y1:y2, x1:x2]

            if acre == OPEN_GROUND and np.sum(subfield==TREES) >= 3:
                new_landscape[y, x] = TREES
            elif acre == TREES and np.sum(subfield==LUMBERYARD) >= 3:
                new_landscape[y, x] = LUMBERYARD
            elif acre == LUMBERYARD:
                if np.sum(subfield==LUMBERYARD) >= 2 and np.sum(subfield==TREES) >= 1:
                    new_landscape[y, x] = LUMBERYARD
                else:
                    new_landscape[y, x] = OPEN_GROUND

    landscape = copy.deepcopy(new_landscape)

print(new_landscape)
print(np.sum(landscape==TREES), np.sum(landscape==LUMBERYARD), np.sum(landscape==TREES) * np.sum(landscape==LUMBERYARD))