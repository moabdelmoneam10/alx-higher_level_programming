#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for subM in matrix:
        print()
        for i in range(len(subM)):
            print("{:d}".format(subM[i]), end='\n' if i is len(subM) - 1 else " ")
