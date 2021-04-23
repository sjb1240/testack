def multiply_vector_by_scalar(vec, n):
    return [n*c for c in vec]


def multiply_matrix_by_scalar(mat, n):
    # return [n*c for c in vec for vec in mat]
    return [multiply_vector_by_scalar(row, n) for vec in mat]


def multiply_matrix_by_matrix(a, b):
    pass


def transpose(matrix):
    pass


def add_matrix(A, B):
    pass


def print_matrix(matrix):
    for row in matrix:
        # print(row)
        for a in row:
            print(a, end=" ")
        print()


mat = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]
print_matrix(mat)

# print(multiply_vector_by_scalar([1, 1, 1, 1], 3))

# print(multiply_matrix_by_scalar([[1, 1], [1, 1]], 2))