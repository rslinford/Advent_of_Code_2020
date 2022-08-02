
def load_instructions(filename):
    with open(filename, 'r') as f:
        data = [x.split(' ') for x in f.read().split('\n')]
        # Add a counter to each instruction for tracking
        # how many times it is called.
        for instruction in data:
            instruction.append(0)
    return data


def run(code, starting_index=0, global_accumulator=0):
    index = starting_index
    while index < len(code):
        # Instructions are allowed to run at most once.
        if code[index][2] > 0:
            return global_accumulator
        code[index][2] += 1
        match code[index][0]:
            case 'nop':
                pass
            case 'acc':
                global_accumulator += int(code[index][1])
            case 'jmp':
                next_index = index + int(code[index][1])
                return run(code, next_index, global_accumulator)
        index += 1
    return global_accumulator


def part_one():
    code = load_instructions('Day_08_data.txt')
    acc = run(code)
    print(f'Accumulator: {acc}')

part_one()
