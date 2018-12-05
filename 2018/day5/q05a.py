
def read_input(file):
    with open(file) as f:
        lines = f.read()
    return lines


def react_polymer(polymer) -> int:
    length = len(polymer)
    i = 0

    while i < (length - 1):
        current = polymer[i]
        next_c = polymer[i+1]

        if current != next_c and current.lower() == next_c.lower():
            polymer = polymer.replace(current + next_c, '')
            i = 0
            length = len(polymer)
        else:
            i += 1

    return len(polymer)

def remove_unit(polymer):
    unique_units = ''.join(set(polymer.lower()))
    
    tested_polymers = {}

    for letter in unique_units:
        tested_polymers[letter] = react_polymer(polymer.replace(letter, '').replace(letter.upper(), ''))
    
    return tested_polymers[(min(tested_polymers, key=tested_polymers.get))]

assert react_polymer('abBA') == 0
assert react_polymer('abAB') == 4
assert react_polymer('aabAAB') == 6
assert react_polymer('dabAcCaCBAcCcaDA') == 10

assert remove_unit('dabAcCaCBAcCcaDA') == 4

question_data = read_input('/home/todd/code/AdventOfCode/2018/data/day05.txt')

print(react_polymer(question_data))
print(remove_unit(question_data))