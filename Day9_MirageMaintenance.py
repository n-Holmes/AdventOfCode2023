from time import time

def read_seqs(path):
    with open(path) as f:
        return [[int(x) for x in line.strip().split()] for line in f.readlines()]

def get_next(sequence):
    rows = [sequence]
    while not all(x == 0 for x in rows[-1]):
        last_row = rows[-1]
        rows.append([b-a for a, b in zip(last_row, last_row[1:])])
    
    rows[-1].append(0)
    for i in range(len(rows) - 2, -1, -1):
        rows[i].append(rows[i][-1] + rows[i + 1][-1])
    
    return rows[0][-1]


def part1(path):
    seqs = read_seqs(path)
    
    # Polynomial sequences (of the same length) form a linear space - add them all up
    seq_sum = [sum(items) for items in zip(*seqs)]

    return get_next(seq_sum)

def part2(path):
    seqs = read_seqs(path)
    
    seq_sum = [sum(items) for items in zip(*seqs)]

    return get_next(list(reversed(seq_sum)))

if __name__ == '__main__':
    start = time()
    print("Part 1: ", part1("input9.txt"), time() - start)
    start = time()
    print("Part 2: ", part2("input9.txt"), time() - start)
