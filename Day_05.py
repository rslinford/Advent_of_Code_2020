import unittest


def FB_to_decimal(value):
    binary = []
    for c in value[0:7]:
        match c:
            case 'F':
                binary.append('0')
            case 'B':
                binary.append('1')
            case _:
                raise ValueError(f'{c} is not an "F" or "B"')
    return int(''.join(binary), 2)


def LR_to_decimal(value):
    binary = []
    for c in value[7:]:
        match c:
            case 'L':
                binary.append('0')
            case 'R':
                binary.append('1')
            case _:
                raise ValueError(f'{c} is not an "L" or "R"')
    return int(''.join(binary), 2)


def calc_unique_seat_id(line):
    return LR_to_decimal(line) + 8 * FB_to_decimal(line)

class TestSeatFinder(unittest.TestCase):
    def test_FB_to_decimal(self):
        with open('Day_05_data_short.txt', 'r') as f:
            for i, line in enumerate(f):
                line = line.strip()
                match i:
                    case 0:
                        self.assertEqual(44, FB_to_decimal(line))
                        self.assertEqual(5, LR_to_decimal(line))
                        self.assertEqual(357, calc_unique_seat_id(line))
                    case 1:
                        self.assertEqual(70, FB_to_decimal(line))
                        self.assertEqual(7, LR_to_decimal(line))
                        self.assertEqual(567, calc_unique_seat_id(line))
                    case 2:
                        self.assertEqual(14, FB_to_decimal(line))
                        self.assertEqual(7, LR_to_decimal(line))
                        self.assertEqual(119, calc_unique_seat_id(line))
                    case 2:
                        self.assertEqual(102, FB_to_decimal(line))
                        self.assertEqual(4, LR_to_decimal(line))
                        self.assertEqual(820, calc_unique_seat_id(line))

def part1():
    filename = 'Day_05_data.txt'
    max_seat_id = 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if calc_unique_seat_id(line) > max_seat_id:
                max_seat_id = calc_unique_seat_id(line)
            print(f'{line} -> row {FB_to_decimal(line)}  column {LR_to_decimal(line)}  seat ID {calc_unique_seat_id(line)}')
    print(f'Max seat ID: {max_seat_id}')


def find_my_seat(ids):
    for i in range(len(ids)):
        if i < 1 or i > len(ids) - 2:
            continue
        if ids[i-1] + 1 == ids[i]:
            continue
        if ids[i+1] - 1 == ids[i]:
            return ids[i] - 1
    return None


def part2():
    filename = 'Day_05_data.txt'
    ids = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            ids.append(calc_unique_seat_id(line))
    ids.sort()
    seat_ID = find_my_seat(ids)
    print(f'My seat is: {seat_ID}')

part2()
