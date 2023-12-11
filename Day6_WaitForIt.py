from time import time
from math import ceil, floor

def get_races(path):
    with open(path) as f:
        lines = f.readlines()[:2]
    
    lines = [[int(x) for x in line.strip().split()[1:]] for line in lines]
    return list(zip(*lines))

def solve_quad(a, b, c):
    # solve a quadratic formula
    chunk = (b*b - 4*a*c)**0.5

    x1 = (-b + chunk) / (2 * a)
    x2 = (-b - chunk) / (2 * a)

    return x1, x2

def count_wins(max_time, high_score):
    low, high = solve_quad(-1, max_time, -high_score)
    if (low == int(low)):
        low = int(low) + 1
    else:
        low = ceil(low)
    
    if (high == int(high)):
        high = int(high) - 1
    else:
        high = floor(high)
    
    if high > low:
        return high - low + 1
    return 0

def part1(path):
    races = get_races(path)

    options = 1
    for max_time, high_score in races:
        # our distance is charge_time * (max_time - charge_time)
        win_count = count_wins(max_time, high_score)
        options *= win_count
    
    return options

def get_races_2(path):
    with open(path) as f:
        lines = f.readlines()[:2]
    
    return [int(line.strip().replace(' ', '').split(':')[1]) for line in lines]

def part2(path):
    max_time, high_score = get_races_2(path)
        
    return count_wins(max_time, high_score)


if __name__ == '__main__':
    start = time()
    print("Part 1: ", part1("input6.txt"), time() - start)
    start = time()
    print("Part 2: ", part2("input6.txt"), time() - start)
