import matrix as m
import unittest


class test_matrix(unittest.TestCase):

    def test_multiply_vector_by_scalar(self):
        self.assertEqual(m.multiply_vector_by_scalar(
            [1, 1, 1, 1], 3), [3, 3, 3, 3])
        self.assertEqual(m.multiply_vector_by_scalar(
            [0, 1, 2, 3, 4], 2), [0, 2, 4, 6, 8])
        self.assertEqual(m.multiply_vector_by_scalar(
            [1, 1, 1, 1, 1], -2), [-2, -2, -2, -2, -2])

    def test_multiply_matrix_by_scalar(self):
        mat = m.multiply_matrix_by_scalar([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 2)
        mat2 = m.multiply_matrix_by_scalar(
            [[12, 1000, 1], [2345, 1, 1], [1, 981234, 12309]], 0)
        r1 = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        r2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(mat, r1)
        self.assertEqual(mat2, r2)

    def test_add_matrix(self):
        m1 = [[1, 1, 1], [2, 2, 2], [1, 1, 1]]
        m2 = [[5, 5, 5], [1, 1, 1], [3, 3, 3]]
        mat = m.add_matrix(m1, m2)
        r = [[6, 6, 6], [3, 3, 3], [4, 4, 4]]
        self.assertEqual(mat, r)

    def test_transpose_matrix(self):
        mat = m.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        res = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(mat, res)

    def test_multiply_matrix_by_matrix(self):
        m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        mat = m.multiply_matrix_by_matrix(m1, m2)
        mat2 = m.multiply_matrix_by_matrix(m1, m1)
        res2 = [[30, 36, 42], [66, 81, 96], [102, 126, 150]]
        res = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(mat, res)
        self.assertEqual(mat2, res2)


if __name__ == "__main__":
    unittest.main()
