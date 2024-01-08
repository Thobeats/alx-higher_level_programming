#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 0:
        i = 0
        for i in range(len(matrix)):
            j = 0
            for j in range(len(matrix[i])):
                if j == 0:
                    print("{:d}".format(matrix[i][j]), end='')
                else:
                    print(" {:d}".format(matrix[i][j]), end='')
                if j == len(matrix[i]) - 1:
                    print()
    else:
        print()
