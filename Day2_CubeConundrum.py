from time import time

def get_game(line):
    game = []
    if not line:
        return 0, []
    
    line = line[5:]
    num_text, game_text = line.split(': ')
    game_num = int(num_text)

    pulls = game_text.split('; ')
    for pull in pulls:
        red = 0
        green = 0
        blue = 0

        for colour in pull.split(', '):
            count_text, colour_text = colour.split(' ')
            count = int(count_text)
            if colour_text[0] == 'r':
                red = count
            elif colour_text[0] == 'g':
                green = count
            else:
                blue = count
        
        game.append((red, green, blue))
    
    return game_num, game


def part1(path):
    with open(path) as f:
        lines = f.readlines()
    
    valid_score = 0
    for line in lines:
        id, game = get_game(line)
        maximums = tuple(map(max, zip(*game)))
        if maximums[0] <= 12 and maximums[1] <= 13 and maximums[2] <= 14:
            valid_score += id
    
    return valid_score


def part2(path):
    with open(path) as f:
        lines = f.readlines()
    
    score = 0
    for line in lines:
        id, game = get_game(line)
        maximums = tuple(map(max, zip(*game)))
        score += maximums[0] * maximums[1] * maximums[2]
    
    return score
    

if __name__ == '__main__':
    start = time()
    print(part1("input2.txt"), time() - start)
    start = time()
    print(part2("input2.txt"), time() - start)
