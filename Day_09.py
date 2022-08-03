def find_pair_part_one(data, preamble_length, target_value_index):
    target_value = data[target_value_index]
    for j in range(target_value_index - preamble_length, target_value_index):
        for i in range(target_value_index - preamble_length, target_value_index):
            if data[j] == data[i]:
                continue
            if data[j] + data[i] == target_value:
                return True, target_value, (data[j], data[i])
    return False, target_value, (0, 0)


def part1():
    for i in range(preamble_length, len(data)):
        found, target_value, matching_pair = find_pair_part_one(data, preamble_length, i)
        if not found:
            print(f'The first number that doesn\'t add up: {target_value}')
            break


doing_short = False
if doing_short:
    preamble_length = 5
    filename = 'Day_09_small_data.txt'
    target_value = 127
else:
    preamble_length = 25
    filename = 'Day_09_data.txt'
    target_value = 1309761972

with open(filename, 'r') as f:
    data = []
    for line in f:
        line = line.strip()
        data.append(int(line))

def find_max_and_min_in_range(data, start_index, end_index):
    return max(data[start_index:end_index]), min(data[start_index:end_index], )

def find_pair_part_two(data, target_value):
    for sequences_of_n_length in range(2, len(data)):
        for starting_index in range(0, len(data)-sequences_of_n_length):
            running_total = 0
            for i in range(starting_index, starting_index + sequences_of_n_length):
                running_total += data[i]
            if running_total == target_value:
                print(f'Matching sequence of length {sequences_of_n_length} found.')
                return find_max_and_min_in_range(data, starting_index, starting_index + sequences_of_n_length)


def part2():
    max_number, min_number = find_pair_part_two(data, target_value)
    print(f'Max number in sequence: {max_number}  Min number: {min_number}  Which add up to {max_number+min_number}')


part2()
