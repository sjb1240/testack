import matrix
# -------------------------------------------------
# Multiply a vector by a scalar
# -------------------------------------------------

# vec1 = [0, 1, 2, 3, 4]
# vec2 = [259, 1234, 12]
# scal1 = 2
# scal2 = 100
# r1 = [0, 2, 4, 6, 8]
# r2 = [25900, 123400, 1200]
# if (matrix.multiply_vector_by_scalar(vec1, scal1) == r1) and (matrix.multiply_vector_by_scalar(vec2, scal2) == r2):
#     print("Passed all test cases")
# else:
#     print("Failed one or more test cases")

# -------------------------------------------------
# multiply a matrix by a scalar
# -------------------------------------------------

# mat1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# scal1 = 2
# res1 = [[0, 2, 4], [6, 8, 10], [12, 14, 16]]

# mat2 = [[10, 20, 30], [1, 2, 3], [0, 0, 0]]
# scal2 = 10
# res2 = [[100, 200, 300], [10, 20, 30], [0, 0, 0]]

# if (matrix.multiply_matrix_by_scalar(mat1, scal1) == res1) and (matrix.multiply_matrix_by_scalar(mat2, scal2) == res2):
#     print("Passed all test cases")
# else:
#     print("Failed one or more test cases")

# -------------------------------------------------
# transpose a matrix
# -------------------------------------------------

# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# res = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# if (matrix.transpose(mat) == res):
#     print("Passed all test cases")
# else:
#     print("Failed one or more test cases")

# -------------------------------------------------
# Multiply a matrix by another matrix
# -------------------------------------------------

# m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# m2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# res = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# res2 = [[30, 36, 42], [66, 81, 96], [102, 126, 150]]

# if (matrix.multiply_matrix_by_matrix(m1, m2) == res) and (matrix.multiply_matrix_by_matrix(m1, m1) == res2):
#     print("Passed all test cases")
# else:
#     print("Failed one or more test cases")
