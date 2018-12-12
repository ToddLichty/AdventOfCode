
offset = 200
initial_state = '.'*offset + '###..###....####.###...#..#...##...#..#....#.##.##.#..#.#..##.#####..######....#....##..#...#...#.#' + '.'*offset

rules = [
    '..#.#',
    '##...',
    '.#...',
    '####.',
    '.##..',
    '.####',
    '.###.',
    '#####',
    '..#..',
    '###..',
    '#..##',
    '##.##',
    '.#..#',
    '#.#..',
    '#.###',
    '#.##.',
    '.#.##',
    '...#.',
    '..##.',
    '##.#.',
]

def next_generation(current_state):
    global rules

    end = len(current_state)
    next_state = list('.' * end)

    for i in xrange(0, end + 3):
        pat = ''

        if i == 0:
            pat = '..' + ''.join(current_state[i:3])
        elif i == 1:
            pat = '.' + ''.join(current_state[i-1:4])
        else:
            pat = ''.join(current_state[i-2:i+3])
        
        if len(pat) < 5:
            pat = pat.ljust(5, '.')

        if pat in rules:
            next_state[i] = '#'

    for i in range(4):
        next_state.append('.')

    return next_state

def sum_of_pots(current_state):
    sum_ = 0
    for x in range(len(current_state)):
        if current_state[x] == '#':
            sum_ += (x - offset)
    return sum_

current_state = list(initial_state)

for x in range(1, 101):
    current_state = next_generation(current_state)
    print(x, s, past_sum, s - past_sum)

print(sum_of_pots(current_state) + ((50000000000 - 100) * 186))