#!/usr/bin/python3
""" Divides the values in a matrix """
def matrix_divided(matrix, div):
    """ checks for the state of the arguments """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if not all(isinstance(i, list) and all(isinstance(j, (int, float)) for j in i) for i in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_sizes = set(len(row) for row in matrix)
    if (len(row_sizes)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    newMatrix = list(map(lambda ir: list(map(lambda val: round(val/div, 2), ir)), matrix))
    return newMatrix
