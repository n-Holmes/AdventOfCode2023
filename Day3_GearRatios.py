from time import time

def get_numbers_and_symbols(path):
    with open(path) as f:
        lines = f.readlines()
    
    numbers = []
    symbols = []

    for i, line in enumerate(lines):
        acc = ''
        for j, char in enumerate(line.strip()):
            if '0' <= char <= '9':
                acc += char
            else:
                # Not a number
                # Was this the end of a number?
                if acc:
                    numbers.append((i, j - len(acc), len(acc), int(acc)))
                    acc = ''
                
                if char != '.':
                    symbols.append((i, j, char))
        
        # Was there a number at the end of the line?
        if acc:
            numbers.append((i, j - len(acc), len(acc), int(acc)))

    return numbers, symbols


def part1(path):
    numbers, symbols = get_numbers_and_symbols(path)
    
    total = 0
    for i, j, length, val in numbers:
        for x, y, _ in symbols:
            if x < i - 1:
                continue
            elif x > i + 1:
                break

            if y >= j - 1 and y <= j + length:
                total += val
                break

    return total


def part2(path):
    numbers, symbols = get_numbers_and_symbols(path)
    
    total = 0
    gears = [(i, j) for i, j, char in symbols if char == '*']

    for x, y in gears:
        adj = []
        for i, j, length, val in numbers:
            if i < x - 1:
                continue
            elif i > x + 1:
                break

            if y >= j - 1 and y <= j + length:
                adj.append(val)
        
        if len(adj) == 2:
            total += adj[0] * adj[1]

    return total
    
    

if __name__ == '__main__':
    start = time()
    print(part1("input3.txt"), time() - start)
    start = time()
    print(part2("input3.txt"), time() - start)
