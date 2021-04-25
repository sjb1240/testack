def multiply_vector_by_scalar(vec, n):
    return [n*c for c in vec]


def multiply_matrix_by_scalar(mat, n):
    # return [n*c for c in vec for vec in mat]
    return [multiply_vector_by_scalar(row, n) for vec in mat]


def multiply_matrix_by_matrix(a, b):
    pass


def transpose(matrix):
    mat_transpose = [[None]*len(matrix)] * len(matrix[0])
    for a in range(len(matrix[0])):
        for b in range(len(matrix)):
            mat_transpose[a][b] = matrix[b][a]
    print_matrix(mat_transpose)    

def add_matrix(A, B):
    if len(A) == len(B):
        sum_matrix = [None]*len(A)
        for a in range(len(A)):
            sum_matrix[a] = add_vectors(A[a], B[a])
    print_matrix(sum_matrix)

#add single column/row vectors
def add_vectors(A,B):
    if len(A) == len(B):
        new_vector = [None]*len(A)
        for a in range(len(A)):
            new_vector[a] = A[a] + B[a]
        return new_vector

def print_matrix(matrix):
    for row in matrix:
        # print(row)
        for a in row:
            print(a, end=" ")
        print()


def print_matrix2(A):
    for row in A:
        row_str = ''.join(str(a) + ' ' for a in row)
        print(row_str)


mat = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]
print_matrix(mat)
print('---------')
print_matrix2(mat)

# print(multiply_vector_by_scalar([1, 1, 1, 1], 3))

# print(multiply_matrix_by_scalar([[1, 1], [1, 1]], 2))
