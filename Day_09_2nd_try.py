import unittest

import numpy as np

def read_dimensions(filename):
    width, height = 0, 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            height += 1
            if len(line) > width:
                width = len(line)
    return width, height


def read_initial_state(filename):
    width, height = read_dimensions(filename)
    grid = np.zeros(((1, 1, height, width)), dtype=int)
    with open(filename, 'r') as f:
        for y, line in enumerate(f):
            line = line.strip()
            for x, c in enumerate(line):
                if c == '.':
                    pass
                elif c == '#':
                    grid[0][0][y][x] = 1
                else:
                    raise(ValueError, f'Found {c}  Expected a . or #')

        grid = grow_grid(grid)
        return grid

offsets = [
    (-1, -1, -1, -1), (-1, -1, -1, 0), (-1, -1, -1, 1),
    (-1, -1, 0, -1),  (-1, -1, 0, 0),  (-1, -1, 0, 1),
    (-1, -1, 1, -1),  (-1, -1, 1, 0),  (-1, -1, 1, 1),

    (-1, 0, -1, -1),  (-1, 0, -1, 0), (-1, 0, -1, 1),
    (-1, 0, 0, -1),   (-1, 0, 0, 0 ), (-1, 0, 0, 1),
    (-1, 0, 1, -1),   (-1, 0, 1, 0),  (-1, 0, 1, 1),

    (-1, 1, -1, -1),  (-1, 1, -1, 0), (-1, 1, -1, 1),
    (-1, 1, 0, -1),   (-1, 1, 0, 0),  (-1, 1, 0, 1),
    (-1, 1, 1, -1),   (-1, 1, 1, 0),  (-1, 1, 1, 1),

    (0, -1, -1, -1), (0, -1, -1, 0), (0, -1, -1, 1),
    (0, -1, 0, -1),  (0, -1, 0, 0),  (0, -1, 0, 1),
    (0, -1, 1, -1),  (0, -1, 1, 0),  (0, -1, 1, 1),

    (0, 0, -1, -1), (0, 0, -1, 0), (0, 0, -1, 1),
    (0, 0, 0, -1),                 (0, 0, 0, 1),
    (0, 0, 1, -1),  (0, 0, 1, 0),  (0, 0, 1, 1),

    (0, 1, -1, -1), (0, 1, -1, 0), (0, 1, -1, 1),
    (0, 1, 0, -1),  (0, 1, 0, 0),  (0, 1, 0, 1),
    (0, 1, 1, -1),  (0, 1, 1, 0),  (0, 1, 1, 1),

    (1, -1, -1, -1), (1, -1, -1, 0), (1, -1, -1, 1),
    (1, -1, 0, -1),  (1, -1, 0, 0),  (1, -1, 0, 1),
    (1, -1, 1, -1),  (1, -1, 1, 0),  (1, -1, 1, 1),

    (1, 0, -1, -1), (1, 0, -1, 0), (1, 0, -1, 1),
    (1, 0, 0, -1),  (1, 0, 0, 0),  (1, 0, 0, 1),
    (1, 0, 1, -1),  (1, 0, 1, 0),  (1, 0, 1, 1),

    (1, 1, -1, -1), (1, 1, -1, 0),  (1, 1, -1, 1),
    (1, 1, 0, -1),  (1, 1, 0, 0),   (1, 1, 0, 1),
    (1, 1, 1, -1),  (1, 1, 1, 0),   (1, 1, 1, 1)
]

def tally_active_neighbors(grid, w, z, y, x):
    tally = 0
    for offset in offsets:
        if grid[w + offset[0]][z + offset[1]][y + offset[2]][x + offset[3]] == 1:
            tally += 1
    return tally

def perform_cycle(grid):
    grid = grow_grid(grid)
    r_grid = np.zeros(grid.shape, dtype=int)
    for w in range(1, grid.shape[0] - 1):
        for z in range(1, grid.shape[1] - 1):
            for y in range(1, grid.shape[2] - 1):
                for x in range(1, grid.shape[3] - 1):
                    tally = tally_active_neighbors(grid, w, z, y, x)
                    is_active = grid[w][z][y][x] == 1
                    if is_active:
                        if tally == 2 or tally == 3:
                            r_grid[w][z][y][x] = 1
                        else:
                            r_grid[w][z][y][x] = 0
                    else:
                        if tally == 3:
                            r_grid[w][z][y][x] = 1
                        else:
                            r_grid[w][z][y][x] = 0

    return r_grid

def perform_six_cycles(grid):
    for _ in range(6):
        grid = perform_cycle(grid)

    print(f'Total active after 6 cycles: {grid.sum()}')
    return grid

def grow_grid(grid):
    return np.pad(grid, ((1, 1), (1, 1), (1, 1), (1, 1)), 'constant')


def render_grid(grid):
    rval = []
    for w in range(0, grid.shape[0]):
        rval.append(f'****  w = {w}  ****\n')
        for z in range(0, grid.shape[1]):
            rval.append(f'z = {z}\n')
            for y in range(0, grid.shape[2]):
                for x in range(0, grid.shape[3]):
                    if grid[w][z][y][x] == 1:
                        rval.append('#')
                    else:
                        rval.append('.')
                rval.append('\n')
            rval.append('\n')
        rval.append('\n')
    return ''.join(rval)


def part1():
    grid = read_initial_state('Day_09_data.txt')
    print('Initial state')
    print(render_grid(grid))
    grid = perform_cycle(grid)
    print('Cycle 1')
    print(render_grid(grid))
    grid = perform_cycle(grid)
    print('Cycle 2')
    print(render_grid(grid))
    grid = perform_cycle(grid)
    print('Cycle 3')
    print(render_grid(grid))
    grid = perform_cycle(grid)
    print('Cycle 4')
    print(render_grid(grid))
    grid = perform_cycle(grid)
    print('Cycle 5')
    print(render_grid(grid))
    grid = perform_cycle(grid)
    print('Cycle 6')
    print(render_grid(grid))
    print(f'Total active after 6 cycles: {grid.sum()}')


part1()

class TestConway(unittest.TestCase):
    def test_read_dimensions(self):
        width, height = read_dimensions('Day_09_short_data.txt')
        self.assertEqual(3, width)
        self.assertEqual(3, height)

    def test_read_initial_state(self):
        grid = read_initial_state('Day_09_short_data_2.txt')
        self.assertEqual((3, 3, 5, 5), grid.shape)
        self.assertEqual(1, grid[1][1][3][3])

    def test_grow_grid(self):
        grid = read_initial_state('Day_09_short_data_2.txt')
        self.assertEqual((3, 3, 5, 5), grid.shape)
        self.assertEqual(0, grid[1][1][0][0])
        self.assertEqual(1, grid[1][1][1][1])
        grid = grow_grid(grid)
        self.assertEqual((5, 5, 7, 7), grid.shape)
        self.assertEqual(0, grid[1][2][1][1])
        self.assertEqual(0, grid[1][2][2][2])
        self.assertEqual(0, grid[1][2][4][2])

    def test_perform_cycle(self):
        grid = read_initial_state('Day_09_short_data.txt')
        grid = perform_cycle(grid)
        self.assertEqual(0, grid[1][1][1][1])
        self.assertEqual(1, grid[1][1][3][2])
        self.assertEqual(0, grid[1][0][1][1])
        self.assertEqual(1, grid[1][1][3][2])
        self.assertTrue(grid.any())

    def test_perform_six_cycle(self):
        grid = read_initial_state('Day_09_short_data.txt')
        grid = perform_six_cycles(grid)
        self.assertTrue(112, grid.sum())

    def test_tally_active_neighbors(self):
        grid = read_initial_state('Day_09_short_data_2.txt')
        tally = tally_active_neighbors(grid, 1, 1, 0, 0)
        self.assertEqual(1, tally)
        tally = tally_active_neighbors(grid, 1, 1, 2, 2)
        self.assertEqual(8, tally)
        tally = tally_active_neighbors(grid, 1, 1, 3, 1)
        self.assertEqual(2, tally)
