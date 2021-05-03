#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List


def independent_zeros(matrix: List[List[float]]):
    size = len(matrix)
    visited_rows = []
    visited_cols = []
    zeros_position = []
    for row in range(size):
        for col in range(size):
            if (matrix[row][col] == 0) and (row not in visited_rows) and (col not in visited_cols):
                zeros_position.append((row, col))
                visited_rows.append(row)
                visited_cols.append(col)
    return zeros_position


def deleting_independent_zeros(A):
    wiersze = []
    kolumny = []
    f = True
    A_ = A[:]
    while f:
        f = False
        for i in range(len(A)):
            if 'o*' not in A[i] and i not in wiersze:
                wiersze.append(i)
                f = True
        for j in range(len(A[0])):
            for k in wiersze:
                if A[k][j] is None and j not in kolumny:
                    kolumny.append(j)
                    f = True
        for i in range(len(A)):
            for k in kolumny:
                if A[i][k] == 'o*' and i not in wiersze:
                    wiersze.append(i)
                    f = True
    wiersze2 = []
    for i in range(len(A)):
        if i not in wiersze:
            wiersze2.append(i)
    return wiersze2, kolumny


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_matrix = [[5, 4, 8, 6],
             [0, 6, 0, 6],
             [4, 3, 2, 7],
             [3, 6, 0, 2]]

    print(independent_zeros(test_matrix))

