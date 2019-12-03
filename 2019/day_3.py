import math 
class WirePoints:
    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.steps = steps
        self.point = (x, y)

    def __str__(self):
        return str(self.point) + ', ' + str(self.steps)

    def __repr__(self):
        return str(self.point) + ', ' + str(self.steps)


def read_input(file):
    with open(file) as f:
        lines = f.readlines()
    
    return [(x.strip()) for x in lines] 


def get_points_visited(wire_path):
    steps = 0
    points_visited = []

    x = y = 0

    for vector in wire_path:
        direction = vector[0]
        distance = int(vector[1:])

        if direction == 'R':
            for _ in range(1, distance + 1):
                steps += 1
                points_visited.append(WirePoints(x + _, y, steps))

            x += distance
        elif direction == 'L':
            for _ in range(1, distance + 1):
                steps += 1
                points_visited.append(WirePoints(x - _, y, steps))

            x -= distance
        elif direction == 'U':
            for _ in range(1, distance + 1):
                steps += 1
                points_visited.append(WirePoints(x, y + _, steps))

            y += distance
        else:
            for _ in range(1, distance + 1):
                steps += 1
                points_visited.append(WirePoints(x, y - _, steps))

            y -= distance
        
    return points_visited


def get_closest_distance(wire_1, wire_2):
    points_visited_1 = get_points_visited(wire_1.split(','))
    points_visited_2 = get_points_visited(wire_2.split(','))

    return min(list(int(math.fabs(s[0]) + math.fabs(s[1])) for s in list(set([wp.point for wp in points_visited_1]).intersection([wp.point for wp in points_visited_2]))))


def get_minimum_steps(wire_1, wire_2):
    points_visited_1 = get_points_visited(wire_1.split(','))
    points_visited_2 = get_points_visited(wire_2.split(','))

    intersecting_points = (list(set([wp.point for wp in points_visited_1]).intersection([wp.point for wp in points_visited_2])))

    min_steps = 9999999999
    for point in intersecting_points:
        wp_1 = [x for x in points_visited_1 if x.point == point][0]
        wp_2 = [x for x in points_visited_2 if x.point == point][0]
        total_steps = wp_1.steps + wp_2.steps

        if total_steps < min_steps:
            min_steps = total_steps

    
    return min_steps

assert(get_closest_distance('R8,U5,L5,D3', 'U7,R6,D4,L4') == 6)
assert(get_closest_distance('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83') == 159)
assert(get_closest_distance('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7') == 135)

question_input = read_input('./2019/data/day_3.in')

print("Answer for question 1: ", get_closest_distance(question_input[0], question_input[1]))

assert(get_minimum_steps('R8,U5,L5,D3', 'U7,R6,D4,L4') == 30)
assert(get_minimum_steps('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83') == 610)
assert(get_minimum_steps('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7') == 410)

print("Answer for question 2: ", get_minimum_steps(question_input[0], question_input[1]))