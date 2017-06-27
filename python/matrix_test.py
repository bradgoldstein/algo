# Tests for matrix.py
#
# Author: Bradley Goldstein

import matrix

import unittest


class TestMatrix(unittest.TestCase):
  def testMatrix_instantiation_createsEmptyMatrix(self):
    m = matrix.Matrix(2, 3)
    self.assertEqual(m[0], [0, 0, 0])
    self.assertEqual(m[1], [0, 0, 0])
    self.assertEqual(m[0][0], 0)
    self.assertEqual(m[1][2], 0)

  def testMatrix_rowOutOfBounds_throwsIndexError(self):
    m = matrix.Matrix(3, 2)
    self.assertRaises(IndexError, m.__getitem__, 3)

  def testMatrix_columnOutOfBounds_throwsIndexError(self):
    col = matrix.Matrix(3, 2)[0]
    self.assertRaises(IndexError, col.__getitem__, 2)

  def testMatrix_setCellInMatrix_updatesCell(self):
    m = matrix.Matrix(2, 3)
    m[1][2] = -3
    m[0][2] = 'a'
    m[1][0] = 4.0
    self.assertEqual(m.matrix_, [[0, 0, 'a'], [4.0, 0, -3]])

  def testMatrix_multiplication_doesProperMultiplication(self):
    m1 = matrix.Matrix(2, 2)
    m1[0][0] = 1
    m1[0][1] = 2
    m1[1][0] = -3
    m1[1][1] = 0
    # m1 = [[ 1, 2],
    #        -3, 0]]

    m2 = matrix.Matrix(2, 3)
    m2[0][0] = 1
    m2[0][1] = 3
    m2[0][2] = -1
    m2[1][0] = 2
    m2[1][1] = 0
    m2[1][2] = 4
    # m2 = [[1, 3, -1],
    #       [2, 0,  4]]

    self.assertEqual((m1*m2).matrix_, [[ 5,  3, 7],
                                       [-3, -9, 3]])

if __name__ == '__main__':
    unittest.main()
