from time import time
from math import lcm

def get_graph(path):
    with open(path) as f:
        instructions, _, *lines = f.readlines()
    
    graph = {line[:3] : (line[7:10], line[12:15]) for line in lines}
    return instructions.strip(), graph

def part1(path):
    instructions, graph = get_graph(path)
    inst_count = len(instructions)

    current = 'AAA'
    inst_index = 0

    while current != 'ZZZ':
        direction = instructions[inst_index % inst_count]

        if direction == 'L':
            current = graph[current][0]
        else:
            current = graph[current][1]

        inst_index += 1

    return inst_index


def part2(path):
    instructions, graph = get_graph(path)
    inst_count = len(instructions)

    currents = [node for node in graph if node[2] == 'A'] 

    # After looking at the input, each start node only encounters one end node.
    # The loop time of each end node is the same as the time to reach it in the first
    # instance.
    loop_sizes = []
    for start_node in currents:
        node = start_node
        inst_index = 0

        while node[2] != 'Z':
            direction = instructions[inst_index % inst_count]
            inst_index += 1
            if direction == 'L':
                node = graph[node][0]
            else:
                node = graph[node][1]
        
        loop_sizes.append(inst_index)

    return lcm(*loop_sizes)

if __name__ == '__main__':
    start = time()
    print("Part 1: ", part1("input8.txt"), time() - start)
    start = time()
    print("Part 2: ", part2("input8.txt"), time() - start)
