import re
from collections import defaultdict

points = []

def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    for line in lines:
<<<<<<< HEAD
        [x, y, vx, vy] = list(map(int, re.findall(r"[-\d]+",line)))
        points.append((x, y, vx, vy))
=======
<<<<<<< c16f0b90f6bbfc60dcceebfe5b75d2ce2f20a592
        [x,y,vx,vy] = list(map(int, re.findall(r"[-\d]+",line)))
        points.append((x,y,vx,vy))
=======
        [x, y, vx, vy] = list(map(int, re.findall(r"[-\d]+",line)))
        points.append((x, y, vx, vy))
>>>>>>> completed day 10
>>>>>>> faafa2896e289d0ada347e20dd73273c4adffb33

def update():
    result = []
    for x, y, vx, vy in points:
        result.append((x + vx, y + vy, vx, vy))    
    
    return result

<<<<<<< HEAD
=======
<<<<<<< c16f0b90f6bbfc60dcceebfe5b75d2ce2f20a592
def display_image():
    x0 = min(x[0] for x in points)
    x1 = max(x[0] for x in points)
    y0 = min(x[1] for x in points)
    y1 = max(x[1] for x in points)

    dx = x1 - x0
    dy = y1 - y0

    p = set((x[0], x[1]) for x in points)

    rows = []
    for y in range(y0, y1 + 1):
        row = []
        for x in range(x0, x1 + 1):
            if (x, y) in p:
                row.append("X")
            else:
                row.append(".")
        rows.append(''.join(row))
    return '\n'.join(rows)


=======
>>>>>>> completed day 10
>>>>>>> faafa2896e289d0ada347e20dd73273c4adffb33
read_input('/home/todd/code/AdventOfCode/2018/data/day10.txt')

i = 0
while True:
    i += 1
    points = update()

    no_solos = True
    mapping = defaultdict(bool)

    for (pos_x, pos_y, _, _) in points:
        mapping[(pos_x, pos_y)] = True

    for (pos_x, pos_y) in mapping:
        if not any((pos_x + delta, pos_y + delta2) in mapping for delta in xrange(-1, 2) for delta2 in xrange(-1, 2) if (delta, delta2) != (0, 0)):
            no_solos = False
            break

    if no_solos:
        min_x = min(z[0] for z in mapping)
        min_y = min(z[1] for z in mapping)
        max_x = max(z[0] for z in mapping)
        max_y = max(z[1] for z in mapping)

        for y in xrange(min_y, max_y+1):
            s = []
            for x in xrange(min_x, max_x+1):
                if mapping[(x, y)]:
                    s.append('#')
                else:
                    s.append('.')
            print(''.join(s))
        
        print(i)