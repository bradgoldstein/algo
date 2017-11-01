# A matrix class for representing a 2-dimensional matrix.
#
# Author: Bradley Goldstein

import random

import numpy as np

POWERS_OF_TWO = [2 ** n for n in range(10)]


class Matrix(object):
  def __init__(self, num_rows=0, num_columns=0):
    self.matrix_ = []
    for x in range(num_rows):
      self.matrix_.append([0 for _ in range(num_columns)])

  def __nonzero__(self):
    return self.matrix_ != []

  def empty(self):
    return not self.__nonzero__()

  def __eq__(self, other):
    if not isinstance(other, Matrix):
      return False

    if self.empty():
      return other.empty()

    if self.numRows is not other.numRows or self.numCols is not other.numCols:
      return False

    for i in range(self.numRows):
      for j in range(self.numCols):
        if self[i][j] != other[i][j]:
          return False

    return True

  def equalSize(self, other):
    return self.numRows == other.numRows and self.numCols == other.numCols

  def __getitem__(self, column_index):
    return self.matrix_[column_index]

  def __add__(self, other):
    if isinstance(other, Matrix):
      return self.view + other.view

    raise TypeError

  def __sub__(self, other):
    if isinstance(other, Matrix):
      return self.view - other.view

    raise TypeError

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

  @property
  def numRows(self):
    return 0 if self.empty() else len(self.matrix_)

  @property
  def numCols(self):
    return 0 if self.empty() else len(self.matrix_[0])

  @property
  def square(self):
    return self.numCols == self.numRows

  @property
  def view(self):
    return _MatrixView(self.matrix_, 0, self.numRows-1, 0, self.numCols-1)

  @classmethod
  def ofSize(cls, m):
    if not isinstance(m, Matrix):
      raise TypeError('Attempting to create a matrix the size of an object which is not a matrix')

    return cls(m.numRows, m.numCols)

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
      assert len(row) is self.numCols, 'Row to append must be the same width as the matrix.'
    self.matrix_.append(row)

  def _appendCol(self, col):
    if self.empty():
      for val in col:
        self.matrix_.append([val])
      return
    assert len(col) is self.numRows, 'Column to append must be the same height as the matrix.'
    for i, val in enumerate(col):
      self.matrix_[i].append(val)

  def getEquivalentNumpyMatrix(self):
    return np.array(self.matrix_)

  def _linearCellOperation(self, other, out, op):
    for i in range(self.numRows):
      for j in range(self.numCols):
        out[i][j] = self[i][j].op(other[i][j])

  def _matrixMultiply(self, other):
    if self.numCols != other.numRows:
      raise ValueError('Attempting to matrix multiply where M1.num_cols != M2.num_rows')

    if self._eligibleForSquareMatrixMultiplyRecursive(other):
      return self._squareMatrixMultiplyResursive(other)

    return self._squareMatrixMultiply(other)

  def _eligibleForSquareMatrixMultiplyRecursive(self, other):
    return self.square and self.equalSize(other) and self.numRows in POWERS_OF_TWO

  def _getMatrixView(self, top_row=None, bottom_row=None, leftmost_col=None, rightmost_col=None):
    if not top_row:
      top_row = 0
    if not bottom_row:
      bottom_row = self.numRows - 1
    if not leftmost_col:
      leftmost_col = 0
    if not rightmost_col:
      rightmost_col = self.numCols - 1
    return _MatrixView(self.matrix_, top_row, bottom_row, leftmost_col, rightmost_col)

  def _squareMatrixMultiplyResursive(self, m2):
    out = Matrix(self.numRows, self.numCols)
    Matrix._squareMatrixMultiplyRecursiveHelper(self._getMatrixView(), m2._getMatrixView(), out._getMatrixView())
    return out

  @staticmethod
  def _squareMatrixMultiplyRecursiveHelper(A_view, B_view, C_view):

    if A_view.size == (1, 1):
      # Base case
      C_view.set(0, 0, C_view.at(0, 0) + A_view.at(0, 0) * B_view.at(0, 0))

    else:
      top_left_a, top_right_a, bottom_left_a, bottom_right_a = A_view.partition()
      top_left_b, top_right_b, bottom_left_b, bottom_right_b = B_view.partition()
      top_left_c, top_right_c, bottom_left_c, bottom_right_c = C_view.partition()

      # C_11 = A_11 * B_11 + A_12 * B_21
      Matrix._squareMatrixMultiplyRecursiveHelper(top_left_a, top_left_b, top_left_c)
      Matrix._squareMatrixMultiplyRecursiveHelper(top_right_a, bottom_left_b, top_left_c)

      # C_12 = A_11 * B_12 + A_12 * B_22
      Matrix._squareMatrixMultiplyRecursiveHelper(top_left_a, top_right_b, top_right_c)
      Matrix._squareMatrixMultiplyRecursiveHelper(top_right_a, bottom_right_b, top_right_c)

      # C_21 = A_21 * B_11 + A_22 * B_21
      Matrix._squareMatrixMultiplyRecursiveHelper(bottom_left_a, top_left_b, bottom_left_c)
      Matrix._squareMatrixMultiplyRecursiveHelper(bottom_right_a, bottom_left_b, bottom_left_c)

      # C_22 = A_21 * B_12 + A_22 * B_22
      Matrix._squareMatrixMultiplyRecursiveHelper(bottom_left_a, top_right_b, bottom_right_c)
      Matrix._squareMatrixMultiplyRecursiveHelper(bottom_right_a, bottom_right_b, bottom_right_c)

  def _createSubmatrix(self, row_index, col_index, size):
    out = Matrix(size, size)
    for i in range(size):
      for j in range(size):
        out[i][j] = self[row_index + 1][col_index + i]
    return out

  def _squareMatrixMultiply(self, other):
    # Naive algorithm to multiply matrices: 'Square-Matrix-Mutliply'
    #
    # See p.75-76 in CLRS 3rd ed.
    out = Matrix(self.numRows, other.numCols)
    for i in range(self.numRows):
      for j in range(other.numCols):
        cell_i_j = 0
        for k in range(self.numCols):  # or other.numRows()
          cell_i_j += self[i][k] * other[k][j]
        out[i][j] = cell_i_j
    return out


class _MatrixView(object):
  def __init__(self, m, top_row, bottom_row, leftmost_col, rightmost_col):
    self.m = m
    self.top_row = top_row
    self.leftmost_col = leftmost_col
    self._height = bottom_row - top_row + 1
    self._width = rightmost_col - leftmost_col + 1

  def equalSize(self, other):
    return self._height == other._height and self._width == other._width

  @property
  def square(self):
    return self._height == self._width

  @property
  def size(self):
    return (self._height, self._width)

  def at(self, row, col):
    return self.m[self.top_row + row][self.leftmost_col + col]

  def set(self, row, col, val):
    self.m[self.top_row + row][self.leftmost_col + col] = val

  def __add__(self, other):
    if not isinstance(other, _MatrixView):
      raise TypeError

    if not self.equalSize(other):
      raise ValueError('Attempting to add matrices that are not the same size')

    out = Matrix(self._height, self._width)
    for i in range(self._height):
      for j in range(self._width):
        out[i][j] = self.m[self.top_row + i][self.leftmost_col + j] \
                    + other.m[other.top_row + i][other.leftmost_col + j]
    return out

  def __sub__(self, other):
    if not isinstance(other, _MatrixView):
      raise TypeError

    if not self.equalSize(other):
      raise ValueError('Attempting to subtract matrices that are not the same size')

    out = Matrix(self._height, self._width)
    for i in range(self._height):
      for j in range(self._width):
        out[i][j] = self.m[self.top_row + i][self.leftmost_col + j] \
                    - other.m[other.top_row + i][other.leftmost_col + j]
    return out

  def partition(self):
    if not self.square:
      raise ValueError('Attempting to partition non-square')

    if not self._height % 2 == 0:
      raise ValueError('Attempting to partition matrix with odd row/column sizes')

    partitioned_size = self._width / 2
    top_left =  _MatrixView(self.m,
                            self.top_row,
                            self.top_row + partitioned_size - 1,
                            self.leftmost_col,
                            self.leftmost_col + partitioned_size - 1)
    top_right = _MatrixView(self.m,
                            self.top_row,
                            self.top_row + partitioned_size - 1,
                            self.leftmost_col + partitioned_size,
                            self.leftmost_col + self._width - 1)
    bottom_left = _MatrixView(self.m,
                               self.top_row + partitioned_size,
                               self.top_row + self._height - 1,
                               self.leftmost_col,
                               self.leftmost_col + partitioned_size - 1)
    bottom_right = _MatrixView(self.m,
                               self.top_row + partitioned_size,
                               self.top_row + self._height - 1,
                               self.leftmost_col + partitioned_size,
                               self.leftmost_col + self._width - 1)
    return (top_left, top_right, bottom_left, bottom_right)