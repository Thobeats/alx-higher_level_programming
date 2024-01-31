#!/usr/bin/python3
""" Divides the values in a matrix """


def matrix_divided(matrix, div):
    """ checks for the state of the arguments """

    emsg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(emsg)
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(emsg)
    # if not all(isinstance(i, list)and
    # all(isinstance(j, (int, float)) for j in i)
    # for i in matrix):
    row_sizes = set(len(row) for row in matrix)
    if (len(row_sizes)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for i in matrix:
        matrix_value = []
        for j in i:
            matrix_value.append(round(j/div, 2))
        new_matrix.append(matrix_value)
    return new_matrix
    # return list(map(lambda ir: list(map(lambda val:
    # round(val/div, 2), ir)), matrix))
