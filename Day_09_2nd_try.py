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
    grid = np.zeros((height, width), dtype=int)
    with open(filename, 'r') as f:
        for y, line in enumerate(f):
            line = line.strip()
            for x, c in enumerate(line):
                if c == '.':
                    pass
                elif c == '#':
                    grid[y][x] = 1
                else:
                    raise(ValueError, f'Found {c}  Expected a . or #')

        grid = np.pad(grid, ((1, 1), (1, 1)), 'constant')
        return grid


def grow_grid(grid):
    return np.pad(grid, ((1, 1), (1, 1)), 'constant')

def part1():
    slice = read_initial_state('Day_09_short_data.txt')

part1()

class TestConway(unittest.TestCase):
    def test_read_dimensions(self):
        width, height = read_dimensions('Day_09_short_data.txt')
        self.assertEqual(3, width)
        self.assertEqual(3, height)

    def test_read_initial_state(self):
        grid = read_initial_state('Day_09_short_data_2.txt')
        self.assertEqual((5,5), grid.shape)
        self.assertEqual(1, grid[3][3])
        print(grid)

    def test_grow_grid(self):
        grid = read_initial_state('Day_09_short_data_2.txt')
        self.assertEqual((5, 5), grid.shape)
        self.assertEqual(0, grid[0][0])
        self.assertEqual(1, grid[1][1])
        grid = grow_grid(grid)
        self.assertEqual((7, 7), grid.shape)
        self.assertEqual(0, grid[1][1])
        self.assertEqual(1, grid[2][2])
        self.assertEqual(1, grid[4][2])

