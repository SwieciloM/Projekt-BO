#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List
import math
from copy import deepcopy


def reduce_matrix(matrix: List[List[float]]):
    new_matrix = deepcopy(matrix)
    rows = len(new_matrix)
    cols = len(new_matrix[0])
    red_sum = 0
    # reduce rows
    for r in range(rows):
        min_el = min(new_matrix[r])
        red_sum += min_el
        for c in range(cols):
            new_matrix[r][c] -= min_el
    # reduce cols
    for c in range(cols):
        min_el = math.inf
        for r in range(rows):
            if new_matrix[r][c] < min_el:
                min_el = new_matrix[r][c]
        red_sum += min_el
        for r in range(rows):
            new_matrix[r][c] -= min_el
    return new_matrix, red_sum


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
                if A[k][j] == 0 and j not in kolumny:
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


def algorytm(matrix, cost):
    n = len(matrix)
    ind_zeros = independent_zeros(matrix)  # wyznaczenie zer niezależnych
    signed_matrix = deepcopy(matrix)  # oznakowanie zer niezależnych jako o*
    for i, j in ind_zeros:
        signed_matrix[i][j] = 'o*'

    rows, cols = deleting_independent_zeros(signed_matrix)  # wyznaczanie zbioru linii wykreślających wszystkie zera w macierzy

    if (len(rows) + len(cols)) == n:
        print("Zera niezależne:", ind_zeros)
        print("Koszt:", cost)
    else:
        # krok 4
        # wykreślanie linii z macierzy
        for i in rows:
            for j in range(n):
                signed_matrix[i][j] = math.inf
        for j in cols:
            for i in range(n):
                signed_matrix[i][j] = math.inf

        # a. wyszukiwanie najmniejszego elementu nie przykrytego liniami
        min_el = math.inf
        for i in range(n):
            for j in range(n):
                if signed_matrix[i][j] < min_el:
                    min_el = signed_matrix[i][j]

        # b. odejmowanie tego elementu od nie przykrytych elementów
        for r in range(n):
            for c in range(n):
                if signed_matrix[r][c] != math.inf:
                    matrix[r][c] -= min_el

        # c. dodanie min_el do elementów przykrytych 2 liniami
        if len(rows) > 0 and len(cols) > 0:
            for r in rows:
                for c in cols:
                    matrix[r][c] += min_el
        # d. zwiększenie wartości kosztu o min_el
        cost += min_el

        algorytm(matrix, cost)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_matrix = [[5, 4, 8, 6],
             [0, 6, 0, 6],
             [4, 3, 2, 7],
             [3, 6, 0, 3]]

    matrix, cost = reduce_matrix(test_matrix)   # redukcja macierzy

    algorytm(matrix, cost)
