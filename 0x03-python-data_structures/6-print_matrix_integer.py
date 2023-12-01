#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for rows in range(len(matrix)):
            for items in range(len(matrix[rows])):
                if items != len(matrix[rows]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[rows][items]), end=endspace)
            print()
