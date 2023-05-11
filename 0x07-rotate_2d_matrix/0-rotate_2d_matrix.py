#!/usr/bin/python3


""" A module that rotates a n x n matrix """


def rotate_2d_matrix(matrix):
    """rotating matrix by 90"""

    copy_matrix = matrix.copy()
    matrix.clear()

    for idx in range(len(copy_matrix)):
        tmp_row = []
        for row in copy_matrix:
            tmp_row.append(row[idx])

        tmp_row.reverse()
        matrix.append(tmp_row)

""" when idx is 0   when idx 1  when idx is 2
    1, 4, 7         2, 5, 8     3, 6, 9
    
    7, 4, 1         8, 5, 2     9, 6, 3
"""



if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
