# Example using the Xpress Python interface
#
# Sudoku: place numbers from 1 to 9 into a 9x9 grid such that no
# number repeats in any row, in any column, and in any 3x3 sub-grid.
#
# More generally, replace 3 with q and 9 with q^2
#
# (C) Fair Isaac Corp., 1983-2023

from __future__ import print_function

import xpress as xp

# We model this problem as an assignment problem where certain
# conditions must be met for all numbers in the columns, rows, and
# sub-grids.
#
# These subgrids are lists of tuples with the coordinates of each
# subgrid. In a 9x9 sudoku, for instance, subgrids[0,1] has the 9
# elements in the top square, i.e., the following:
#
#  ___ ___ ___
# |   |###|   |
# |   |###|   |
# |___|###|___|
# |   |   |   |
# |   |   |   |
# |___|___|___|
# |   |   |   |
# |   |   |   |
# |___|___|___|
#
# while subgrids[2,2] has the 9 elements in the bottom right square.

# The input is a starting grid where the unknown numbers are replaced by zero

q = 3

starting_grid = \
 [[0, 0, 5, 0, 0, 0, 0, 4, 0],
  [0, 0, 4, 0, 0, 3, 5, 0, 8],
  [0, 6, 8, 0, 0, 4, 3, 0, 1],
  [0, 0, 0, 6, 8, 0, 0, 3, 0],
  [0, 0, 2, 0, 0, 0, 8, 0, 0],
  [0, 3, 0, 0, 2, 9, 0, 0, 0],
  [5, 0, 7, 2, 0, 0, 1, 8, 0],
  [6, 0, 9, 5, 0, 0, 4, 0, 0],
  [0, 8, 0, 0, 0, 0, 2, 0, 0]]


def get_solutions_sudoku():

    n = q**2  # the size must be the square of the size of the subgrids
    N = range(n)

    x = {(i, j, k): xp.var(vartype=xp.binary, name='x{0}_{1}_{2}'.format(i, j, k))
        for i in N for j in N for k in N}

    # define all q^2 subgrids
    subgrids = {(h, l): [(i, j) for i in range(q*h, q*h + q)
                for j in range(q*l, q*l + q)]
                for h in range(q)
                for l in range(q)}

    vertical = [xp.Sum(x[i, j, k] for i in N) == 1 for j in N for k in N]
    horizontal = [xp.Sum(x[i, j, k] for j in N) == 1 for i in N for k in N]
    subgrid = [xp.Sum(x[i, j, k] for (i, j) in subgrids[h, l]) == 1
            for (h, l) in subgrids.keys() for k in N]

    # Assign exactly one number to each cell

    assign = [xp.Sum(x[i, j, k] for k in N) == 1 for i in N for j in N]

    # Fix those variables that are non-zero in the input grid

    init = [x[i, j, k] == 1 for k in N for i in N for j in N
            if starting_grid[i][j] == k+1]

    p = xp.problem()

    p.addVariable(x)
    p.addConstraint(vertical, horizontal, subgrid, assign, init)

    # we don't need an objective function, as long as a solution is found

    p.optimize()

    return p, x