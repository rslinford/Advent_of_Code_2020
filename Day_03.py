import re


def load_puzzle_data(filename):
    rval = []
    with open(filename, 'r') as f:
        for line in f:
            rval.append(line.strip())
    return rval

def part1():
    data = load_puzzle_data('Day_03.txt')
    x, y = 0, 0
    trees_encountered = 0
    for line in data:
        width = len(line)
        if line[x % width] == '#':
            trees_encountered += 1
            line = line[0:x % width] + 'X' + line[x % width:]
        else:
            line = line[0:x % width] + 'O' + line[x % width:]
        x += 3
        print(line, trees_encountered)

def part2():
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    trees_encountered_record = []
    for slope in slopes:
        trees_encountered = 0
        x, y = 0, 0
        data = load_puzzle_data('Day_03.txt')
        xd, yd = slope[0], slope[1]
        for line in data:
            if y % yd != 0:
                print(f'{y:4}) {line} {xd, yd}')
                x += xd
                y += 1
                continue
            width = len(line)
            if line[x % width] == '#':
                trees_encountered += 1
                line = line[0:x % width] + 'X' + line[x % width + 1:]
            else:
                line = line[0:x % width] + 'O' + line[x % width + 1:]
            x += xd
            y += 1

            print(f'{y:4}) {line} {xd, yd}')
        trees_encountered_record.append(trees_encountered)
        print(f'Trees Encountered {trees_encountered} {trees_encountered_record}')
    answer = 1
    for x in trees_encountered_record:
        answer *= x
    print(answer)

part2()
"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.

4997836800 is wrong
"""
