from time import time

def get_cards(path):
    with open(path) as f:
        lines = f.readlines()
    
    cards = []
    for line in lines:
        _, line = line.split(': ')
        winning, numbers = line.strip().split(' | ')
        winning = tuple(map(int, winning.split()))
        numbers = tuple(map(int, numbers.split()))
        cards.append((winning, numbers))

    return cards


def part1(path):
    cards = get_cards(path)
    
    total = 0
    for winning, ours in cards:
        count = count = len(set(winning).intersection(ours))
        if count:
            total += 1 << (count - 1)

    return total


def part2(path):
    cards = get_cards(path)

    num_cards = len(cards)

    counts = [1] * num_cards
    for i, (winning, ours) in enumerate(cards):
        if i > len(counts):
            break

        win_count = len(set(winning).intersection(ours))
        for j in range(i + 1, min(i + win_count + 1, num_cards)):
            counts[j] += counts[i]
    
    return sum(counts)

if __name__ == '__main__':
    start = time()
    print(part1("input4.txt"), time() - start)
    start = time()
    print(part2("input4.txt"), time() - start)
