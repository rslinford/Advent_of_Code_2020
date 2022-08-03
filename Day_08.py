
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


def run2(code, starting_index=0, global_accumulator=0):
    index = starting_index
    while index < len(code):
        # Instructions are allowed to run at most once.
        if code[index][2] > 0:
            return global_accumulator, False
        code[index][2] += 1
        match code[index][0]:
            case 'nop':
                pass
            case 'acc':
                global_accumulator += int(code[index][1])
            case 'jmp':
                next_index = index + int(code[index][1])
                return run2(code, next_index, global_accumulator)
        index += 1
    return global_accumulator, True


def part_one():
    code = load_instructions('Day_08_data.txt')
    acc = run(code)
    print(f'Accumulator: {acc}')

def flip_instruction(code, nth):
    n = 0
    for i, instruction in enumerate(code):
        if instruction[0] == 'nop' or instruction[0] == 'jmp':
            n += 1
            if n == nth:
                if instruction[0] == 'nop':
                    code[i][0] = 'jmp'
                else:
                    code[i][0] = 'nop'
                break

def part_two():
    i = 0
    normal_termination = False
    while not normal_termination:
        i += 1
        code = load_instructions('Day_08_data.txt')
        flip_instruction(code, i)
        acc, normal_termination = run2(code)
        if normal_termination:
            print(f'Accumulator: {acc}  Normal termination: {normal_termination}')

part_two()
