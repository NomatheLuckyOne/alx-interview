#!/usr/bin/python3

"""A function that returns the perimeter of the island 
described in grid"""

def island_perimeter(grid):
	""" grid is rectangular, with its width and heigth not 
	exceeding 100 """
	whole_perimeter = 0

	for idx, row in enumerate(grid):
	        for elem_idx, elements in enumerate(row):
            		if (elements == 0):
                		continue

            		# left
            		if (elem_idx != 0 and row[elem_idx - 1] == 0):
                		whole_perimeter += 1

            		# left
            		if (elem_idx == 0):
                		whole_perimeter += 1

            		# right
            		if (elem_idx != len(row) - 1 and row[elem_idx + 1] == 0):
                		whole_perimeter += 1
           	 	# right
            		if elem_idx == len(row) - 1:
                		whole_perimeter += 1

            		# top
            		if idx != 0 and grid[idx - 1][elem_idx == 0]:
                		whole_perimeter += 1
            		# top
            		if idx == 0:
                		whole_perimeter += 1

            		# bottom
            		if idx != len(grid) -1 and grid[idx + 1][elem_idx == 0]:
                		whole_perimeter += 1

            		if idx == len(grid) -1:
                		whole_perimeter += 1

	return whole_perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
print(island_perimeter(grid))
