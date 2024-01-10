#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = matrix.copy()
    new_matrix = []
    for i in matrix_copy:
        group = []
        for j in i:
            group.append(j**2)
        new_matrix.append(group)
    return new_matrix
