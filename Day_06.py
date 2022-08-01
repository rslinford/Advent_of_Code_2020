



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

def part2():
    filename = 'Day_06_data.txt'
    groups = read_groups(filename)

    tally = 0
    for group in groups:
        group_member_list = group.split('\n')
        s = set()
        for i, group_member in enumerate(group_member_list):
            if i == 0:
                for c in group_member:
                    s.add(c)
            else:
                t = set()
                for c in group_member:
                    t.add(c)
                s = s.intersection(t)
        tally += len(s)
    print(f'The answer is {tally}')
part2()