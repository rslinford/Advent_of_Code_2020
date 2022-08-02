

def read_initial_slice(filename):
    with open(filename, 'r') as f:
        grid = []
        for line in f:
            line = line.strip()
            row = []
            grid.append(row)
            for c in line:
                row.append(c)
        return grid

def render_grid(grid):
    rval = []
    for row in grid:
        rval.append(''.join(row))
        rval.append('\n')
    return ''.join(rval)

def blank_padding(grid):
    padding = []
    width = len(grid[0]) * 10
    height = len(grid) * 10
    return buffer_grid(width, height)

def buffer_grid(width, height):
    return [['.' for _ in range(width)] for _ in range(height)]

def draw_grid_on_padding(grid, padding):
    x_offset = 4 * len(grid[0])
    y_offset = 4 * len(grid)
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            padding[y + y_offset][x + x_offset] = grid[y][x]

offsets = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1)]

def one_generation(grid):
    buffer = buffer_grid(len(grid[0]), len(grid))
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            current_is_active = grid[y][x] == '#'
            # count active adjacent squares
            adjacent_active = 0
            for o in offsets:
                if grid[y-o[1]][x-o[0]] == '#':
                    adjacent_active += 1
            # if adjacent_active > 0 or current_is_active:
            #     print(f'({x}, {y}) active({current_is_active}) and has {adjacent_active} active neighbors.')
            if current_is_active:
                if adjacent_active != 2 and adjacent_active != 3:
                    buffer[y][x] = '.'
                else:
                    buffer[y][x] = '#'
            else:
                if adjacent_active == 3:
                    buffer[y][x] = '#'
                else:
                    buffer[y][x] = '.'
    return buffer


def part1():
    original_grid  = read_initial_slice('Day_09_short_data.txt')
    grid = blank_padding(original_grid)
    draw_grid_on_padding(original_grid, grid)
    print('Generation 0\n' + render_grid(grid))
    for i in range(1, 70):
        grid = one_generation(grid)
        print(f'Generation {i}\n{render_grid(grid)}')

part1()