# A matrix class for representing a 2-dimensional matrix.
#
# Author: Bradley Goldstein

import random

import numpy as np

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
    if  self.empty():
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
      return self.matrixMultiply(other)

    # Other types of Matrix multiplication are undefined
    raise TypeError

  def getEquivalentNumpyMatrix(self):
    return np.array(self.matrix_)

  def matrixMultiply(self, other):
    if self.numCols() != other.numRows():
      raise ValueError('Attempting to matrix multiply where M1.num_cols != M2.num_rows')

    # if self.numCols() == self.numRows() == other.numCols() == other.numRows() and powerOf2(self.numRows()):
    #   return self._squareMatrixMultiply(other)
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
