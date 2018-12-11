class Node:
    def __init__(self, name, num_children, num_meta, meta_data=0, parent=None):
        self.name = name
        self.num_children = num_children
        self.num_meta = num_meta
        self.meta_data = []
        self.parent = parent
        self.children = []

    def append(self, child):
        self.children.append(child)

    def __repr__(self):
        return self.name + ' - ' + str(self.num_children)

ns = map(int, open('/home/todd/code/AdventOfCode/2018/data/day08.txt').read().split())
i = 0


def next_int():
    global i
    global ns
    i += 1
    return ns[i-1]


def sum_tree(node):
    sum_ = 0

    for m in node.meta_data:
        sum_ += m

    if node.num_children > 0:
        for c in node.children:
            sum_ += sum_tree(c)

    return sum_

def value(node):
    if node.num_children == 0:
        return sum(node.meta_data)
    else:
        ans = 0
        for m in node.meta_data:
            if 1 <= m <= len(node.children):
                ans += value(node.children[m-1])
        return ans


def build_tree():
    new_node_children, new_node_meta = next_int(), next_int()

    root = Node('root', new_node_children, new_node_meta)

    for _ in range(new_node_children):
        root.children.append(build_tree())

    for _ in range(new_node_meta):
        root.meta_data.append(next_int())

    return root

root = build_tree()
print(sum_tree(root))
print(value(root))