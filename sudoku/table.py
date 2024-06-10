import tkinter as tk
import time


def create_sudoku_table(root, entries):
    table_frame = tk.Frame(root)
    table_frame.pack()

    # Create 9x9 grid of Entry widgets
    for i in range(9):
        row_entries = []
        for j in range(9):
            entry = tk.Entry(table_frame, width=3, font=('Arial', 12))
            entry.grid(row=i, column=j, padx=1, pady=1)
            row_entries.append(entry)
            tk.Entry(textvariable="1")
        entries.append(row_entries)
    root.update()
    time.sleep(0.1)
    return entries


def set_cell_value(row, col, value, entries, root):
    entries[row][col].delete(0, tk.END)
    entries[row][col].insert(0, value)
    root.update()
    time.sleep(0.1)
