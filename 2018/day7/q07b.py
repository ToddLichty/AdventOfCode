
def load_data():
    data = defaultdict(list)
    with Path('/home/todd/code/AdventOfCode/2018/data/day07.txt').open() as f:
        for line in f:
            prereq, step = DATA.search(line).groups()
            data[step].append(prereq)
            if prereq not in data:
                data[prereq] = []
    return data

def get_next(data):
    item = sorted(x for x in data if not data[x])
    if not item:
        return None, 0

    item = item[0]
    del data[item]

    return item, BASE_TIME + ord(item) - ord("A") + 1

BASE_TIME = 60  # base + offset (A == 1, B == 2, ...)
WORKERS = 5  # total number of workers

DATA = re.compile(r"Step (.) must be finished before step (.) can begin")

def remove_item(data, item):
    for v in data.values():
        try:
            i = v.index(item)
        except ValueError:
            continue
        del v[i]

def part2():
    data = load_data()

    time = 0
    workers = [(None, 0)] * WORKERS
    while data:
        time += 1

        # assign work
        for i, t in enumerate(workers):
            if t[1] == 0:
                workers[i] = get_next(data)

        # complete work
        for i, w in enumerate(workers):
            workers[i] = (w[0], max(0, w[1] - 1))
            # if work was assigned, and the timer ran out, then
            # remove the work item from dependency lists
            if workers[i][1] == 0 and w[0]:
                remove_item(data, w[0])

    # final adjustment
    time += max(w[1] for w in workers)
    print("TIME", time)

part2()
