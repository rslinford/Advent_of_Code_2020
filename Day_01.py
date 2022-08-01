

def load_puzzle_data(filename):
    rval = []
    with open(filename, 'r') as f:
        for line in f:
            rval.append(int(line))
    return rval


def part_one():
    data = load_puzzle_data('Day_01_data.txt')
    for i, n in enumerate(data):
        for j, m in enumerate(data):
            if n + m == 2020:
                print(f'{n} + {m} == 2020')
                print(f'{n} * {m} == {n * m}')

def part_two():
    data = load_puzzle_data('Day_01_data.txt')
    for i, n in enumerate(data):
        for j, m in enumerate(data):
            for k, o in enumerate(data):
                if n + m + o == 2020:
                    print(f'{n} + {m} + {o} == 2020')
                    print(f'{n} * {m} * {o} == {n * m * o}')


part_two()