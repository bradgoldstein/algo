# A matrix class for representing a 2-dimensional matrix.
#
# Author: Bradley Goldstein

import random

import numpy as np

POWERS_OF_TWO = [2 ** n for n in range(10)]


def _calculatePartitionIndices(min_row_index, min_col_index, size_of_matrix):
  min_row_index_top = min_row_index
  min_row_index_bottom = min_row_index + size_of_matrix
  min_col_index_left = min_col_index
  min_col_index_right = min_col_index + size_of_matrix
  return min_row_index_top, min_row_index_bottom, min_col_index_left, min_col_index_right


class Matrix(object):
  def __init__(self, num_rows, num_columns):
    self.matrix_ = []
    for x in range(num_rows):
      self.matrix_.append([0 for y in range(num_columns)])

  def __nonzero__(self):
    return self.matrix_ != []

  def empty(self):
    return not self.__nonzero__()

  def __eq__(self, other):
    if not isinstance(other, Matrix):
      return False

    if self.empty():
      return other.empty()

    if self.numRows() is not other.numRows() or self.numCols() is not other.numCols():
      return False

    for i in range(self.numRows()):
      for j in range(self.numCols()):
        if self[i][j] != other[i][j]:
          return False

    return True

  def __getitem__(self, column_index):
    return self.matrix_[column_index]

  def numRows(self):
    return 0 if self.empty() else len(self.matrix_)

  def numCols(self):
    return 0 if self.empty() else len(self.matrix_[0])

  @classmethod
  def fromRows(cls, rows):
    m = cls(0, 0)
    for row in rows:
      m._appendRow(row)
    return m

  @classmethod
  def columnVector(cls, col):
    m = cls(0, 0)
    m._appendCol(col)
    return m

  @classmethod
  def rowVector(cls, row):
    m = cls(0, 0)
    m._appendRow(row)
    return m

  @classmethod
  def randomMatrix(cls, num_rows, num_columns, min_val=0, max_val=10):
    m = cls(num_rows, num_columns)
    for i in range(num_rows):
      for j in range(num_columns):
        m.matrix_[i][j] = random.randint(min_val, max_val)
    return m

  def _appendRow(self, row):
    if not self.empty():
      assert len(row) is self.numCols(), 'Row to append must be the same width as the matrix.'
    self.matrix_.append(row)

  def _appendCol(self, col):
    if self.empty():
      for val in col:
        self.matrix_.append([val])
      return
    assert len(col) is self.numRows(), 'Column to append must be the same height as the matrix.'
    for i, val in enumerate(col):
      self.matrix_[i].append(val)

  def __mul__(self, other):
    if isinstance(other, int) or isinstance(other, float):
      # TODO(bradley): Implement scalar multiplication
      raise NotImplementedError

    if isinstance(other, list):
      # TODO(bradley): Implement vector multiplication
      raise NotImplementedError

    if isinstance(other, Matrix):
      return self._matrixMultiply(other)

    # Other types of Matrix multiplication are undefined
    raise TypeError

  def getEquivalentNumpyMatrix(self):
    return np.array(self.matrix_)

  def _matrixMultiply(self, other):
    if self.numCols() != other.numRows():
      raise ValueError('Attempting to matrix multiply where M1.num_cols != M2.num_rows')

    if self._eligibleForSquareMatrixMultiplyRecursive(other):
      return self._squareMatrixMultiplyResursive(other)

    return self._squareMatrixMultiply(other)

  def _eligibleForSquareMatrixMultiplyRecursive(self, other):
    return self.numCols() == self.numRows() == other.numCols() == other.numRows() and self.numRows() in POWERS_OF_TWO

  def _squareMatrixMultiplyResursive(self, m2):
    out = Matrix(self.numRows(), self.numCols())
    Matrix._squareMatrixMultiplyRecursiveHelper(self, m2, out, 0, 0, 0, 0, 0, 0, self.numRows())
    return out

  def _squareMatrixMultiplyRecursiveHelper(
      A, B, C,
      min_row_index_a, min_col_index_a,
      min_row_index_b, min_col_index_b,
      min_row_index_c, min_col_index_c,
      size_of_matrices):
    # Recursive algorithm to multiply square matrices whose edges are powers of 2: 'Square-Matrix-Mutliply-Recursive'
    #
    # See p.76-79 in CLRS 3rd ed.
    if size_of_matrices == 1:
      C[min_row_index_c][min_col_index_c] = (C[min_row_index_c][min_col_index_c] +
                                             A[min_row_index_a][min_col_index_a] * B[min_row_index_b][min_col_index_b])

    else:
      size_of_matrices_in_next_call = size_of_matrices / 2
      (min_row_top_a, min_row_bottom_a, min_col_left_a, min_col_right_a) = _calculatePartitionIndices(
        min_row_index_a, min_col_index_a, size_of_matrices_in_next_call)
      (min_row_top_b, min_row_bottom_b, min_col_left_b, min_col_right_b) = _calculatePartitionIndices(
        min_row_index_b, min_col_index_b, size_of_matrices_in_next_call)
      (min_row_top_c, min_row_bottom_c, min_col_left_c, min_col_right_c) = _calculatePartitionIndices(
        min_row_index_c, min_col_index_c, size_of_matrices_in_next_call)

      # C_11 = A_11 * B_11 + A_12 * B_21
      Matrix._squareMatrixMultiplyRecursiveHelper(
        A, B, C,
        min_row_top_a, min_col_left_a,
        min_row_top_b, min_col_left_b,
        min_row_top_c, min_col_left_c,
        size_of_matrices_in_next_call)
      Matrix._squareMatrixMultiplyRecursiveHelper(
        A, B, C,
        min_row_top_a, min_col_right_a,
        min_row_bottom_b, min_col_left_b,
        min_row_top_c, min_col_left_c,
        size_of_matrices_in_next_call)

      # C_12 = A_11 * B_12 + A_12 * B_22
      Matrix._squareMatrixMultiplyRecursiveHelper(
        A, B, C,
        min_row_top_a, min_col_left_a,
        min_row_top_b, min_col_right_b,
        min_row_top_c, min_col_right_c,
        size_of_matrices_in_next_call)
      Matrix._squareMatrixMultiplyRecursiveHelper(
        A, B, C,
        min_row_top_a, min_col_right_a,
        min_row_bottom_b, min_col_right_b,
        min_row_top_c, min_col_right_c,
        size_of_matrices_in_next_call)

      # C_21 = A_21 * B_11 + A_22 * B_21
      Matrix._squareMatrixMultiplyRecursiveHelper(
        A, B, C,
        min_row_bottom_a, min_col_left_a,
        min_row_top_b, min_col_left_b,
        min_row_bottom_c, min_col_left_c,
        size_of_matrices_in_next_call)
      Matrix._squareMatrixMultiplyRecursiveHelper(
        A, B, C,
        min_row_bottom_a, min_col_right_a,
        min_row_bottom_b, min_col_left_b,
        min_row_bottom_c, min_col_left_c,
        size_of_matrices_in_next_call)

      # C_22 = A_21 * B_12 + A_22 * B_22
      Matrix._squareMatrixMultiplyRecursiveHelper(
        A, B, C,
        min_row_bottom_a, min_col_left_a,
        min_row_top_b, min_col_right_b,
        min_row_bottom_c, min_col_right_c,
        size_of_matrices_in_next_call)
      Matrix._squareMatrixMultiplyRecursiveHelper(
        A, B, C,
        min_row_bottom_a, min_col_right_a,
        min_row_bottom_b, min_col_right_b,
        min_row_bottom_c, min_col_right_c,
        size_of_matrices_in_next_call)

  def _squareMatrixMultiply(self, other):
    # Naive algorithm to multiply matrices: 'Square-Matrix-Mutliply'
    #
    # See p.75-76 in CLRS 3rd ed.
    out = Matrix(self.numRows(), other.numCols())
    for i in range(self.numRows()):
      for j in range(other.numCols()):
        cell_i_j = 0
        for k in range(self.numCols()):  # or other.numRows()
          cell_i_j += self[i][k] * other[k][j]
        out[i][j] = cell_i_j
    return out
