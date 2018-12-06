from collections import defaultdict, namedtuple


def readInput(file):
    with open(file) as f:
        lines = f.readlines()
    return [(x.strip()) for x in lines] 

def get_coordinates(lines):
    values = namedtuple('coords', 'max_x', 'max_y')
    values.coords = set()
    values.max_x = values.max_y = 0

    for line in lines:
        y, x = map(int, line.split(", "))
        values.coords.add((y, x))
        values.max_y = max(values.max_y, y)
        values.max_x = max(values.max_x, x)

    return values


def get_max_size(lines):
    values = get_coordinates(lines)
    max_x, max_y = values.max_x, values.max_y

    id_to_point = {id: point for id, point in enumerate(values.coords, start=1)}
    region_sizes = defaultdict(int)
    infinite_ids = set()

    for i in range(max_y + 1):
        for j in range(max_x + 1):
            min_dists = sorted([(abs(y - i) + abs(x - j), id) for id, (y, x) in id_to_point.items()])

            if len(min_dists) == 1 or min_dists[0][0] != min_dists[1][0]:
                id = min_dists[0][1]
                region_sizes[id] += 1

                if i == 0 or i == max_y or j == 0 or j == max_x:
                    infinite_ids.add(id)

    return(max(size for id, size in region_sizes.items() if id not in infinite_ids))


def get_size_shared_region(lines, manhattan_limit=10000):
    values = get_coordinates(lines)
    max_x, max_y = values.max_x, values.max_y

    size_shared_region = 0

    for i in range(max_y + 1):
        for j in range(max_x + 1):
            size_shared_region += int(sum(abs(y - i) + abs(x - j) for y, x in values.coords) < manhattan_limit)

    return size_shared_region



lines = [
    '1, 1',
    '1, 6',
    '8, 3',
    '3, 4',
    '5, 5',
    '8, 9',
]

assert get_max_size(lines) == 17
assert get_size_shared_region(lines, 32) == 16

lines = readInput('/home/todd/code/AdventOfCode/2018/data/day06.txt')

print(get_max_size(lines))
print(get_size_shared_region(lines))