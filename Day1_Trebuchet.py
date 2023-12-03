from time import time

numbers = "zero one two three four five six seven eight nine".split()

def get_num(line):
    for char in line:
        if '0' <= char <= '9':
            return char

def get_num_better(line):
    first = None
    last = None
    for i, char in enumerate(line):
        if '0' <= char <= '9':
            val = int(char)
            if first is None:
                first = val
            last = val
        
        for val, number in enumerate(numbers):
            if line[i:].startswith(number):
                if first is None:
                    first = val
                last = val

    return 10 * first + last

def part1(path):
    with open(path) as f:
        lines = f.readlines()
    
    return sum(int(get_num(line) + get_num(reversed(line))) for line in lines)

def part2(path):
    with open(path) as f:
        lines = f.readlines()
    
    total = 0
    for line in lines:
        total += get_num_better(line)

    return total

if __name__ == '__main__':
    start = time()
    print(part1("input1.txt"), time() - start)
    start = time()
    print(part2("input1.txt"), time() - start)
