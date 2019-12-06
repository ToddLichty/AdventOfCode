from collections import defaultdict
from anytree import Node, Walker


def read_input(file):
    with open(file) as f:
        lines = f.readlines()
    
    return [(x.strip()) for x in lines] 


def build_tree(test_input):
    orbits = defaultdict(list)
    orbit_set = set()
    orbit_tree = {}

    for x in test_input:
        parent, child = x.split(')')

        orbit_set.add(parent)
        orbit_set.add(child)
        orbits[parent].append(child)

    for i in orbit_set:
        orbit_tree[i] = Node(i) 

    for key, value in orbits.items():
        orbit_tree[key].children = [orbit_tree[i] for i in value]

    return orbit_tree


def get_total_orbits(orbit_tree):
    total_orbits = 0
    for node in orbit_tree:
        total_orbits += orbit_tree[node].depth

    return total_orbits


def get_transfers(orbit_tree):
    you = orbit_tree['YOU']
    san = orbit_tree['SAN']

    w = Walker()
    route = w.walk(you, san)
    transfers = len(route[0]) + len(route[2]) - 2

    return transfers


test_input = '''B)C
C)D
D)E
E)F
B)G
G)H
COM)B
D)I
E)J
J)K
K)L'''

assert(get_total_orbits(build_tree(test_input.split('\n'))) == 42)

question_input = read_input('./2019/data/day_6.in')
print('Answer to question 1: ', get_total_orbits(build_tree(question_input)))

test_input = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''

assert(get_transfers(build_tree(test_input.split('\n'))) == 4)
print('Answer to question 1: ', get_transfers(build_tree(question_input)))
