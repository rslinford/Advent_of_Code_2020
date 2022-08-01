import re


def load_puzzle_data(filename):
    rval = []
    with open(filename, 'r') as f:
        for line in f:
            result = re.search('^(\d+)-(\d+) (\w+): (\w+)$', line)
            rval.append([int(result.group(1)), int(result.group(2)), result.group(3), result.group(4)])
    return rval

def part_01():
    data = load_puzzle_data('Day_02_data.txt')

    total_right = 0
    for entry in data:
        print(entry)
        minimum, maximum, letter, password = entry[0], entry[1], entry[2], entry[3]

        n = 0
        for c in password:
            if c == letter:
                n += 1
        if n < minimum or n > maximum:
            print('Wrong ' + str(entry))
        else:
            total_right += 1

    print('Answer', total_right)

def part_02():
    data = load_puzzle_data('Day_02_data.txt')
    total_valid = 0
    for entry in data:
        pos1, pos2, letter, password = entry[0], entry[1], entry[2], entry[3]
        pos1 -= 1
        pos2 -= 1
        if (password[pos1]==letter) ^ (password[pos2]==letter):
            print("Right", entry)
            total_valid +=1
        else:
            print("Wrong", entry)
    print("Answer", total_valid)

part_02()
