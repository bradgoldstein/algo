# Tests for matrix.py
#
# Author: Bradley Goldstein

import matrix

import unittest


class TestMatrix(unittest.TestCase):
  def testTruthiness_emptyMatrix_returnsCorrectValues(self):
    m = matrix.Matrix(0, 0)
    m.matrix_ = []

    self.assertFalse(m)
    self.assertFalse(m.__nonzero__())
    self.assertTrue(m.empty())

  def testTruthiness_normalMatrix_returnsCorrectValues(self):
    m = matrix.Matrix(1, 1)
    # m.matrix_ = [[0]]
    #
    self.assertTrue(m)
    self.assertTrue(m.__nonzero__())
    self.assertFalse(m.empty())

  def testEquals_otherIsNotAMatrix_returnsFalse(self):
    m = matrix.Matrix(1, 1)

    self.assertNotEqual(m, [[0]])

  def testEquals_bothAreEmpty_returnsTrue(self):
    m = matrix.Matrix(0, 0)
    other = matrix.Matrix(0, 0)
    other.matrix_ = []

    self.assertEqual(m, other)

  def testEquals_otherIsNotEmpty_returnsFalse(self):
    m = matrix.Matrix(0, 0)
    other = matrix.Matrix(1, 1)

    self.assertNotEqual(m, other)

  def testEquals_otherIsEmpty_returnsFalse(self):
    m = matrix.Matrix(1, 1)
    other = matrix.Matrix(0, 0)

    self.assertNotEqual(m, other)

  def testEquals_otherIsEqual_returnsTrue(self):
    m = matrix.Matrix(1, 2)
    m[0][1] = 'a'
    other = matrix.Matrix(0, 0)
    other.matrix_ = [[0, 'a']]

    self.assertEqual(m, other)

  def testSet_cellInMatrix_updatesCell(self):
    m = matrix.Matrix(2, 3)
    m[1][2] = -3
    m[0][2] = 'a'
    m[1][0] = 4.0

    self.assertEqual(m.matrix_, [[0, 0, 'a'], [4.0, 0, -3]])

  def testInitialization_zeroArguments_createsEmptyMatrix(self):
    m = matrix.Matrix(0, 0)

    self.assertTrue(m.empty())

  def testInitialization_plainInitialization_createsZerosMatrix(self):
    m = matrix.Matrix(2, 3)

    self.assertEqual(m.matrix_, [[0, 0, 0], [0, 0, 0]])

  def testOfSize_regularSize_initializesMatrixOfSameSize(self):
    m = matrix.Matrix(2, 3)
    m[1][1] = 'a'

    n = matrix.Matrix.ofSize(m)

    self.assertEqual(n.matrix_, [[0, 0, 0], [0, 0, 0]])

  def testOfSize_zeroSizes_initializesMatrixOfZeroSize(self):
    m = matrix.Matrix(0, 0)

    n = matrix.Matrix.ofSize(m)

    self.assertTrue(n.empty())

  def testOfSize_nonMatrix_throwsTypeError(self):
    self.assertRaises(TypeError, matrix.Matrix.ofSize, list())

  def testFromRows_normalArguments_createsProperMatrix(self):
    m = matrix.Matrix.fromRows([[1, 2], [3, 4], [5, 6]])

    self.assertEqual(m.matrix_, [[1, 2], [3, 4], [5, 6]])

  def testColumnVector_normalArguments_createsProperMatrix(self):
    m = matrix.Matrix.columnVector([1, 2, 3, 4])

    self.assertEqual(m.matrix_,[[1], [2], [3], [4]])

  def testRowVector_normatArguments_createsProperMatrix(self):
    m = matrix.Matrix.rowVector([1, 2, 3, 4])

    self.assertEqual(m.matrix_, [[1, 2, 3, 4]])

  def testGet_rowOutOfBounds_throwsIndexError(self):
    m = matrix.Matrix(3, 2)

    self.assertRaises(IndexError, m.__getitem__, 3)

  def testGet_columnOutOfBounds_throwsIndexError(self):
    col = matrix.Matrix(3, 2)[0]

    self.assertRaises(IndexError, col.__getitem__, 2)

  def testGetEquivalentNumpyMatrix_normalArguments_createsEquivalentMatrix(self):
    m = matrix.Matrix.randomMatrix(num_rows=3, num_columns=4, max_val=5)

    n = m.getEquivalentNumpyMatrix()

    for i in range(m.numRows):
      for j in range(m.numCols):
        self.assertEqual(m[i][j], n[i][j])

    # Check that changing a value in m does not change a value in n
    m[2][2] = 'a'
    self.assertNotEqual(m[2][2], n[2][2])

  def testAddition_normalArguments_returnsCorrectResult(self):
    m1 = matrix.Matrix.fromRows([[1,  2],
                                 [-3, 0]])
    m2 = matrix.Matrix.fromRows([[1,  3],
                                 [2,  0]])

    m3 = m1 + m2

    self.assertEqual(m3.matrix_, [[ 2, 5],
                                  [-1, 0]])

  def testAddition_emptyMatrices_returnsEmptyMatrix(self):
    m1 = matrix.Matrix(0, 0)
    m2 = matrix.Matrix(0, 0)

    m3 = m1 + m2

    self.assertTrue(m3.empty())

  def testAddition_mismatchedShapes_throwsValueError(self):
    m1 = matrix.Matrix.fromRows([[ 1, 2],
                                 [-3, 0]])
    m2 = matrix.Matrix.fromRows([[1,  3, 1],
                                 [2,  0, 1]])

    self.assertRaises(ValueError, m1.__add__, m2)

  def testAddition_unaddableValues_throwsTypeError(self):
    m1 = matrix.Matrix.fromRows([[ 1, 2],
                                 [-3, 0]])
    m2 = matrix.Matrix.fromRows([[ 1,  3],
                                 [ 2,  'a']])

    self.assertRaises(TypeError, m1.__add__, m2)

  def testSubtraction_normalArguments_returnsCorrectResult(self):
    m1 = matrix.Matrix.fromRows([[ 1, 2],
                                 [-3, 0]])
    m2 = matrix.Matrix.fromRows([[ 1, 3],
                                 [ 2, 0]])

    m3 = m1 - m2

    self.assertEqual(m3.matrix_, [[ 0, -1],
                                  [-5,  0]])

  def testSubtraction_emptyMatrices_returnsEmptyMatrix(self):
    m1 = matrix.Matrix(0, 0)
    m2 = matrix.Matrix(0, 0)

    m3 = m1 - m2

    self.assertTrue(m3.empty())

  def testSubtraction_mismatchedShapes_throwsValueError(self):
    m1 = matrix.Matrix.fromRows([[1,  2],
                                 [-3, 0]])
    m2 = matrix.Matrix.fromRows([[1,  3, 1],
                                 [2,  0, 1]])

    self.assertRaises(ValueError, m1.__sub__, m2)

  def testSubtraction_unaddableValues_throwsTypeError(self):
    m1 = matrix.Matrix.fromRows([[1,  2],
                                 [-3, 0]])
    m2 = matrix.Matrix.fromRows([[1,  3],
                                 [2,  'a']])

    self.assertRaises(TypeError, m1.__sub__, m2)

  def testMultiplication_normalArguments_returnsCorrectResult(self):
    m1 = matrix.Matrix.fromRows([[1, 2],
                                 [-3, 0]])
    m2 = matrix.Matrix.fromRows([[1, 3, -1],
                                 [2, 0, 4]])

    self.assertCorrectMatrixMultiply(m1, m2)

  def testMultiplication_mismatchedRowsAndColumns_raisesValueError(self):
    m1 = matrix.Matrix.fromRows([[1, 2],
                                 [-3, 0]])
    m2 = matrix.Matrix.fromRows([[1, 3],
                                 [2, 0],
                                 [3, 4]])

    self.assertRaises(ValueError, m1.__mul__, m2)

  def testRecursiveMatrixMultiply_twoByTwo_returnsCorrectResult(self):
    m1 = matrix.Matrix.fromRows([[ 1,  2],
                                 [-1,  0,]])
    m2 = matrix.Matrix.fromRows([[ 1, -2],
                                 [-1,  0]])

    self.assertCorrectMatrixMultiply(m1, m2)

  def testRecursiveMatrixMultiply_fourByFour_returnsCorrectResult(self):
    m1 = matrix.Matrix.fromRows([[ 1,  2, -2,  0],
                                 [-1,  0,  1,  1],
                                 [-2, -1,  1, -1],
                                 [-2, -1,  0, -1]])
    m2 = matrix.Matrix.fromRows([[ 1, -2,  3,  0],
                                 [-1,  0, -1, -1],
                                 [ 2,  1,  0,  1],
                                 [-2, -1,  1,  3]])

    self.assertCorrectMatrixMultiply(m1, m2)


  def testRecursiveMatrixMultiply_eightByEight_returnsCorrectResult(self):
    m1 = matrix.Matrix.fromRows([[ 1,  2, -2,  0,  1,  1,  0, -2],
                                 [-1,  0,  1,  1,  1, -2,  1,  1],
                                 [-2, -1,  1, -1, -1,  2, -1,  1],
                                 [-2, -1,  0, -1, -1, -1, -1,  1],
                                 [ 0,  0,  1, -2, -1,  0, -1,  0],
                                 [ 0, -2, -1, -1, -1,  0, -2,  0],
                                 [ 1,  1, -1,  2,  0,  0, -1,  0],
                                 [-2,  1, -1,  0, -1,  0,  1,  0]])
    m2 = matrix.Matrix.fromRows([[ 1, -2,  3,  0,  0, -5,  3, -2],
                                 [-1,  0, -1, -1, -1,  2,  0,  0],
                                 [ 2,  1,  0,  1,  1, -2,  1,  0],
                                 [-2, -1,  1,  3,  1, -1, -1,  0],
                                 [ 0,  1, -1,  0,  1,  0,  1,  0],
                                 [ 1, -2,  1,  1, -1,  0, -2,  0],
                                 [-1, -1, -1,  2,  0, -1,  1,  1],
                                 [ 2,  0,  1,  1,  1,  0,  1,  0]])

    self.assertCorrectMatrixMultiply(m1, m2)

  def assertCorrectMatrixMultiply(self, m1, m2):
    self.assertEqual((m1*m2).matrix_,
                     m1.getEquivalentNumpyMatrix().dot(m2.getEquivalentNumpyMatrix()).tolist())


if __name__ == '__main__':
    unittest.main()
