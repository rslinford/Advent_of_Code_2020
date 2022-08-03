

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
    for slice in grid:
        for row in slice:
            rval.append(''.join(row))
            rval.append('\n')
        rval.append('\n')
    return ''.join(rval)

def blank_padding(grid):
    padding = []
    width = len(grid[0]) * 10
    height = len(grid) * 10
    depth = 5
    return buffer_grid(width, height, depth)

def buffer_grid(width, height, depth):
    return [[['.' for _ in range(width)] for _ in range(height)] for _ in range(depth)]

def draw_grid_on_padding(grid, padding):
    x_offset = 4 * len(grid[0])
    y_offset = 4 * len(grid)
    z_offset = 1
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            padding[z_offset][y + y_offset][x + x_offset] = grid[y][x]

offsets = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1)]

def one_generation(grid):
    print(grid)
    buffer = buffer_grid(len(grid[0]), len(grid), 5)
    for z in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            for x in range(1, len(grid[0][0]) - 1):
                current_is_active = grid[z][y][x] == '#'
                # count active adjacent squares
                adjacent_active = 0
                for o in offsets:
                    if grid[z][y-o[1]][x-o[0]] == '#':
                        adjacent_active += 1
                # if adjacent_active > 0 or current_is_active:
                #     print(f'({x}, {y}) active({current_is_active}) and has {adjacent_active} active neighbors.')
                if current_is_active:
                    if adjacent_active != 2 and adjacent_active != 3:
                        buffer[z][y][x] = '.'
                    else:
                        buffer[z][y][x] = '#'
                else:
                    if adjacent_active == 3:
                        buffer[z][y][x] = '#'
                    else:
                        print(x, y, z)
                        buffer[z][y][x] = '.'
    return buffer


def part1():
    original_grid  = read_initial_slice('Day_17_short_data.txt')
    grid = blank_padding(original_grid)
    draw_grid_on_padding(original_grid, grid)
    print('Generation 0\n' + render_grid(grid))
    for i in range(1, 70):
        grid = one_generation(grid)
        print(f'Generation {i}\n{render_grid(grid)}')

part1()