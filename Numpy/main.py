# YOUR CODE HERE
import numpy as np
with open('matrix.txt', 'r') as f:
    lines = f.readlines()
    n_rows, n_cols = input().split(' ')
    n_rows, n_cols = int(n_rows), int(n_cols)
    rows = []

    lst = []
    for i in lines[:n_rows]:
        values = i.strip().split(' ')
        rows.append(values)

    for j in range(len(rows)):
        col = []
        for k in range(n_cols):
            values = rows[j][k]
            col.append(values)
        lst.append(col)

input_matrix = np.array(lst, dtype=np.int8)
print(input_matrix)
print(np.mean(input_matrix, axis=0))
print(np.mean(input_matrix, axis=1))
