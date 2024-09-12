#!/usr/bin/python3

"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix=[]):
	"""
	Do not return anything. The matrix must be edited in-place.
	You can assume the matrix will have 2 dimensions and will not be empty.
	"""
	outer_list = []
	for i in range(len(matrix)):
		inner_list = []
		for j in matrix.__reversed__():
			inner_list.append(j[i])
		outer_list.append(inner_list)
	
	for k in range(len(matrix)):
		for l in range(len(matrix)):
			matrix[k][l] = outer_list[k][l]

	