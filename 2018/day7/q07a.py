from collections import defaultdict
import pprint
import string
import re
from pathlib import Path

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


instructions = read_input('/home/todd/code/AdventOfCode/2018/data/day07.txt')
print(process_instructions(parse_instructions(instructions)))
