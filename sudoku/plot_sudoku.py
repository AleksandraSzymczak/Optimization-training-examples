import matplotlib.pyplot as plt
import numpy as np

def plot_sudoku_smaller(grid):
    _, ax = plt.subplots(figsize=(4.5, 4.5))
    ax.matshow(np.ones_like(grid) * -1, cmap='Greys', vmin=-1, vmax=9)
    
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                ax.text(j, i, str(grid[i][j]), va='center', ha='center')

    # Draw grid lines
    for i in range(1, 9):
        lw = 2 if i % 3 == 0 else 1
        ax.axhline(i - 0.5, color='black', linewidth=lw)
        ax.axvline(i - 0.5, color='black', linewidth=lw)

    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()
starting_grid = \
 [[8, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 3, 6, 0, 0, 0, 0, 0],
  [0, 7, 0, 0, 9, 0, 2, 0, 0],
  [0, 5, 0, 0, 0, 7, 0, 0, 0],
  [0, 0, 0, 0, 4, 5, 7, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 3, 0],
  [0, 0, 1, 0, 0, 0, 0, 6, 8],
  [0, 0, 8, 5, 0, 0, 0, 1, 0],
  [0, 9, 0, 0, 0, 0, 4, 0, 0]]
plot_sudoku_smaller(starting_grid)