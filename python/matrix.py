# A matrix class for representing a 2-dimensional matrix.
#
# Author: Bradley Goldstein

class Matrix(object):
  def __init__(self, num_rows, num_columns):
    self.matrix_ = []
    for x in range(num_rows):
      self.matrix_.append([0 for y in range(num_columns)])

  def __getitem__(self, column_index):
    return self.matrix_[column_index]

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

  def numRows(self):
    return len(self.matrix_)

  def numCols(self):
    return len(self.matrix_[0])

  def matrixMultiply(self, other):
    if self.numCols() != other.numRows():
      raise ValueError('Attempting to multiple M1 * M2 where M1.num_cols != M2.num_rows')

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

# August 4-26
# 7.5 days off