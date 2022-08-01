"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.

4997836800 is wrong oops
5872458240 is Right! yay
"""

def load_puzzle_data(filename):
    lines = None
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
    return lines

def run():
    data = load_puzzle_data('Day_03.txt')
    width = len(data[0])

    tree_tally = []
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        x = 0
        trees_encountered = 0
        dx, dy = slope
        for j, row in enumerate(data):
            if j % dy != 0:
                continue
            if row[x % width] == '#':
                trees_encountered += 1
                print(row[:x % width] + 'X' + row[x % width + 1:] + ' ' + str(slope))
            else:
                print(row[:x % width] + 'O' + row[x % width + 1:] + ' ' + str(slope))
            x += dx
        tree_tally.append(trees_encountered)
        print(trees_encountered, "For ", slope)
        print()
    print(trees_encountered)
    answer = 1
    for n in tree_tally:
        answer *= n

    print('Answer', answer)

run()

