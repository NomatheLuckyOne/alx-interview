#!/usr/bin/python3
""" A function that returns the perimeter of an island """


def island_perimeter(grid):
    """ return the perimeter of the island """
    whole_perimeter = 0

    for idx, row in enumerate(grid):
        for elem_idx, element in enumerate(row):
            if (element == 0):
                continue

            # Left
            if (elem_idx != 0 and row[elem_idx - 1] == 0):
                whole_perimeter += 1

            if (elem_idx == 0):
                whole_perimeter += 1

            # Right
            if (elem_idx != len(row) - 1 and row[elem_idx + 1] == 0):
                whole_perimeter += 1

	    # right
            if (elem_idx == len(row) - 1):
                whole_perimeter += 1

            # Upper part
            if (idx != 0 and grid[idx - 1][elem_idx] == 0):
                whole_perimeter += 1

            if (idx == 0):
                # top edge case
                whole_perimeter += 1

            # Bottom Check
            if (idx != len(grid) - 1 and grid[idx + 1][elem_idx] == 0):
                whole_perimeter += 1

            if (idx == len(grid) - 1):
                # bottom edge case
                whole_perimeter += 1

    return whole_perimeter
#
#
#if __name__ == "__main__":
#    grid = [
#        [0, 0, 0, 0, 0, 0],
#        [0, 1, 0, 0, 0, 0],
#        [0, 1, 0, 0, 0, 0],
#        [0, 1, 1, 1, 0, 0],
#        [0, 0, 0, 0, 0, 0]
#    ]
#print(island_perimeter(grid))
