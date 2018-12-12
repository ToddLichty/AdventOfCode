from collections import defaultdict
import pprint
import string
<<<<<<< HEAD
=======
<<<<<<< c16f0b90f6bbfc60dcceebfe5b75d2ce2f20a592
import re
from pathlib import Path
=======
>>>>>>> completed day 10
>>>>>>> faafa2896e289d0ada347e20dd73273c4adffb33

class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._child_values = set()
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)
            self._child_values.add(node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, key):
        """ Remove all references to node """
        for value in self._graph[key]:
            if value in self._child_values:
                self._child_values.remove(value)

        try:
            del self._graph[key]
        except KeyError:
            pass

    def get_childless(self):
        keys = self._graph.keys()
        not_found = []

        for k in keys:
            found = False
            for v in self._graph.values():
                if k in v:
                    found = True
                    break
            
            if not found:
                not_found.append(k)

        return(sorted(not_found))

def read_input(file):
    with open(file) as f:
        lines = f.readlines()
    return [(x.strip()) for x in lines] 

def process_instructions(connections) -> str:
    g = Graph(connections, directed=True)

    steps = ''
    while True:
        k = g.get_childless()

        if len(k) == 0:
            return (steps + list(d)[0])
            break
            
        key = k[0]
        d = g._graph[key]
        steps += key
        g.remove(key)

def parse_instructions(instructions):
    connections = []
    for instruction in instructions:
        words = instruction.split()
        t = (words[1], words[7])
        connections.append(t)

    return connections


<<<<<<< c16f0b90f6bbfc60dcceebfe5b75d2ce2f20a592
instructions = read_input('/home/todd/code/AdventOfCode/2018/data/day07.txt')
print(process_instructions(parse_instructions(instructions)))
=======
instructions = {
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.',
}

class Worker:
    def __init__(self):
        self.current_step = ''
        self.finished = -1

def free_worker(workers):
    for worker in workers:
        if worker.current_step == '':
            return worker
    
    return None

num_workers = 2
interval = 0

connections = parse_instructions(instructions)
g = Graph(connections, directed=True)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(g._graph)

workers = []
workers.append(Worker())

second = 0

k = g.get_childless()
last_step = None

while True:
    print("Second = " + str(second))
    #did any step finish?
    for worker in workers:
        if worker.current_step != '':
            if worker.finished <= second:
                print(worker.current_step + ' finished')
                g.remove(worker.current_step)
                pp.pprint(g._graph)
                worker.current_step = ''

    if len(g._graph) == 1:
        last_step = list(g._graph['F'])[0]

    for a in g.get_childless():
        w = free_worker(workers)
        if w != None:
            print('assigning ' + str(a) + ' to worker 0')
            w.current_step = a
            w.finished = second + interval + string.ascii_lowercase.index(a.lower()) + 1

            print(str(a) + ' will take ' + str(w.finished))

    second += 1


# instructions = read_input('/home/todd/code/AdventOfCode/2018/data/day07.txt')
# print(process_instructions(parse_instructions(instructions)))
<<<<<<< HEAD
=======
>>>>>>> completed day 10
>>>>>>> faafa2896e289d0ada347e20dd73273c4adffb33
