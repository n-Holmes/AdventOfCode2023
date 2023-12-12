from time import time
from collections import Counter

def get_hands(path, val_dict):
    with open(path) as f:
        lines = f.readlines()
    
    hands = []
    for line in lines:
        if line:
            hand, bid = line.strip().split()
            hand_nums = tuple(val_dict[c] for c in hand)
            hands.append((hand_nums, int(bid)))
    
    return hands


def score_hand(hand):
    counts = Counter(hand).most_common()
    first_set = counts[0][1]
    second_set = counts[1][1] if len(counts) > 1 else 0
    return 3 * first_set + second_set


def part1(path):
    values = {c : i for i, c in enumerate('0123456789TJQKA')}
    hands = get_hands(path, values)

    hands = sorted(
        (score_hand(hand), hand, bid)
        for hand, bid in hands
    )

    total_score = 0
    for rank, (_, _, bid) in enumerate(hands, 1):
        total_score += rank * bid
    
    return total_score


def score_hand_with_jokers(hand):
    counts = Counter(hand).most_common()
    first_set = counts[0][1]
    second_set = counts[1][1] if len(counts) > 1 else 0

    if counts[0][0] == 0 or (len(counts) > 1 and counts[1][0] == 0):
        # One of our tow largest sets is jokers - add them together
        first_set += second_set
        # The next-largest set is always size 1 or 0
        second_set = 1 if first_set < 5 else 0
    
    elif 0 in hand:
        # We have a single joker (if there were more it would be one of the big sets)
        first_set += 1

    return 3 * first_set + second_set


def part2(path):
    values_joker = {c : i for i, c in enumerate('J_23456789TQKA')}
    hands = get_hands(path, values_joker)

    hands = sorted(
        (score_hand_with_jokers(hand), hand, bid)
        for hand, bid in hands
    )

    total_score = 0
    for rank, (_, _, bid) in enumerate(hands, 1):
        total_score += rank * bid
    
    return total_score



if __name__ == '__main__':
    start = time()
    print("Part 1: ", part1("input7.txt"), time() - start)
    start = time()
    print("Part 2: ", part2("input7.txt"), time() - start)
