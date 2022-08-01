



def read_groups(filename):
    with open(filename, 'r') as f:
        groups = f.read().strip().split('\n\n')
        return groups

def part1():
    filename = 'Day_06_data.txt'
    groups = read_groups(filename)
    yes_tally = 0
    for group in groups:
        u = set()
        for c in group:
            if c == '\n':
                continue
            u.add(c)
        n = len(u)
        yes_tally += n
    print(f'Yes tally {yes_tally}')

def part1():
    filename = 'Day_06_data.txt'
    groups = read_groups(filename)
    s = set()
    for i, group in enumerate(groups):
        if i == 0:
            for c in
part2()