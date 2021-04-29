def multiply_vector_by_scalar(vec, n):
    return [n*c for c in vec]


def multiply_matrix_by_scalar(mat, n):
    # return [n*c for c in vec for vec in mat]
    return [multiply_vector_by_scalar(vec, n) for vec in mat]


def dot_prod(vec_a, vec_b):
    new_vector = [vec_a[i]*vec_b[i] for i in range(len(vec_a))]
    return sum(new_vector)


def multiply_matrix_by_matrix(mat_a, mat_b):
    if len(mat_a[0]) != len(mat_b):
        return False
    mat_b = transpose(mat_b)
    nm = []
    for row in mat_a:
        nm_row = [dot_prod(row, row2) for row2 in mat_b]
        nm.append(nm_row)
    return nm


def transpose(mat):
    new_mat = []
    for i in range(len(mat[0])):
        new_row = [row[i] for row in mat]
        new_mat.append(new_row)
    return new_mat


def print_matrix(mat):
    for row in mat:
        for a in row:
            print(a, end=" ")
        print()


def print_matrix_2(A):
    for row in A:
        row_str = ''.join(str(a) + ' ' for a in row)
        print(row_str)


def add_matrix(mat_a, mat_b):
    new_mat = []
    for i in range(len(mat_a)):
        new_row = []
        for j in range(len(mat_a[i])):
            new_value = mat_a[i][j]+mat_b[i][j]
            new_row.append(new_value)
        new_mat.append(new_row)
    return new_mat


# mat = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]
# print(print_matrix(transpose(mat)))

m1 = [[3, 4, 2]]
m2 = [[13, 9, 7, 15], [8, 7, 4, 6], [6, 4, 0, 3]]
# print_matrix(multiply_matrix_by_matrix(m1, m2))
# print_matrix(add_matrix(m1, m2))


v1 = [1, 2, 3]
v2 = [4, 5, 6]
# print(dot_prod(v1, v2))


# print_matrix(mat)
# print('---------')
# print_matrix_2(mat)

# print(multiply_vector_by_scalar([1, 1, 1, 1], 3))

# print(multiply_matrix_by_scalar([[1, 1], [1, 1]], 2))
