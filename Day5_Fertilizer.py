from time import time

def get_maps(path):
    with open(path) as f:
        text = f.read()
    
    maps = []
    for i, part in enumerate(text.split('\n\n')):
        if i == 0:
            seeds = get_seeds(part)
        else:
            maps.append(get_map(part))

    return seeds, maps

def get_seeds(line):
    return [int(s) for s in line.split(':')[1].strip().split()]

def get_map(chunk):
    mapping = []
    for line in chunk.split('\n')[1:]:
        if line:
            dest, source, count = map(int, line.strip().split())
            mapping.append((source, dest, count))
    
    return mapping

def part1(path):
    seeds, maps = get_maps(path)
    
    current = seeds[:]
    for mapping in maps:
        new = []
        for value in current:
            for source, dest, count in mapping:
                if value >= source and value - source < count:
                    new.append(value - source + dest)
                    break
            else:
                # The mythical for-else! (Executes if loop not broken)
                new.append(value)

        current = new
    
    return min(current)

def sort_and_merge(sections):
    out_sections = sorted(sections)

    i = 1
    while i < len(out_sections):
        start_1, len_1 = out_sections[i-1]
        start_2, len_2 = out_sections[i]
        if start_2 > start_1 + len_1:
            i += 1
        else:
            # Need to merge
            new_len = start_2 + len_2 - start_1
            out_sections[i - 1] = (start_1, new_len)
            out_sections.pop(i)

    return out_sections


def apply_map_single(mapping, section):
    out_sections = []
    
    in_head, in_len = section
    for source, dest, count in sorted(mapping):
        if in_len <= 0:
            break;

        if source > in_head:
            # Some of the range is before the map
            if in_head + in_len <= source:
                # This is the final section of input
                out_sections.append((in_head, in_len))
                in_len = 0
                break
            else:
                part_len = source - in_head
                out_sections.append((in_head, part_len))
                in_head += part_len
                in_len -= part_len
                if in_len <= 0:
                    break;
        
        if in_head > source + count:
            # The map section ends before the input
            continue

        if in_head + in_len <= source + count:
            # remainder of input is within mapped section
            out_sections.append((dest + (in_head - source), in_len))
            in_len = 0
            break
        else:
            # input goes beyond mapped section, add the output of the mapped section
            part_len = source + count - in_head
            out_sections.append((dest + (in_head - source), part_len))
            in_head += part_len
            in_len -= part_len

    # Catch any leftovers after the end of mapping input sections
    if in_len > 0:
        out_sections.append((in_head, in_len))

    return out_sections

def apply_map(mapping, sections):
    out_sections = []
    for section in sections:
        out_sections.extend(apply_map_single(mapping, section))
    
    return sort_and_merge(out_sections)

def part2(path):
    seeds, maps = get_maps(path)
    # Seed ranges are in [start, end) format
    ranges = sort_and_merge([
        (seeds[i], seeds[i + 1])
        for i in range(0, len(seeds), 2)
    ])

    for mapping in maps:
        ranges = apply_map(mapping, ranges)
    
    return ranges[0][0]


if __name__ == '__main__':
    start = time()
    print("Part 1: ", part1("input5.txt"), time() - start)
    start = time()
    print("Part 2: ", part2("input5.txt"), time() - start)
