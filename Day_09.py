def find_pair(data, preamble_length, target_value_index):
    target_value = data[target_value_index]
    for j in range(target_value_index - preamble_length, target_value_index):
        for i in range(target_value_index - preamble_length, target_value_index):
            if data[j] == data[i]:
                continue
            if data[j] + data[i] == target_value:
                return True, target_value, (data[j], data[i])
    return False, target_value, (0, 0)


doing_short = False
if doing_short:
    preamble_length = 5
    filename = 'Day_09_small_data.txt'
else:
    preamble_length = 25
    filename = 'Day_09_data.txt'

with open(filename, 'r') as f:
    data = []
    for line in f:
        line = line.strip()
        data.append(int(line))


def part1():
    for i in range(preamble_length, len(data)):
        found, target_value, matching_pair = find_pair(data, preamble_length, i)
        if not found:
            print(f'The first number that doesn\'t add up: {target_value}')
            break


def part2():
    target_value = 1309761972


