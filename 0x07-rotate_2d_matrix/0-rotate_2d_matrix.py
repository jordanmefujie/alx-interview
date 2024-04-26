#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not
    all(isinstance(row, list) for row in matrix):
        return

    rows = len(matrix)
    cols = len(matrix[0])

    if not all(len(row) == cols for row in matrix):
        return

    new_matrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            new_matrix[j][rows - i - 1] = matrix[i][j]

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = new_matrix[i][j]
