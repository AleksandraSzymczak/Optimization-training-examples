from table import create_sudoku_table, set_cell_value
import tkinter as tk
from sudoku import get_solutions_sudoku


if __name__=="__main__":
    
    q = 3
    n = q**2
    N = range(n)
    root = tk.Tk()
    root.title("Sudoku")
    entries = []

    sudoku_entries = create_sudoku_table(root, entries)
    problem, x = get_solutions_sudoku()
    breakpoint()
    for i in N:
        for j in N:
            l = [k for k in N if problem.getSolution(x[i, j, k]) >= 0.5]
            assert(len(l) == 1)
            print('{0:2d}'.format(1 + l[0]), end='', sep='')
            set_cell_value(row=i, col=j, value=1+l[0], entries=entries, root=root)
        print('')

    root.mainloop()