
# Tests for merge_sort.py
#
# Author: Bradley Goldstein

import merge_sort as merge

import unittest

# Example from CLRS 3rd ed. p.35
CLRS_EXAMPLE = [5, 2, 4, 7, 1, 3, 2, 6]
CLRS_SORTED = sorted(CLRS_EXAMPLE)

class TestMergeSort(unittest.TestCase):
    def testMerge_negativeLeftIndex_throws(self):
        self.assertRaises(AssertionError,
            merge._merge, [0, 1, 2, 3, 4], -1, 2, 3)

    def testMerge_midIndexIsLessThanLeft_throws(self):
        self.assertRaises(AssertionError,
            merge._merge, [0, 1, 2, 3, 4], 2, 1, 3)

    def testMerge_midIndexIsMoreThanRight_throws(self):
        self.assertRaises(AssertionError,
            merge._merge, [0, 1, 2, 3, 4], 0, 2, 1)

    def testMerge_rightIndexIsPastEndOfAray_throws(self):
        self.assertRaises(AssertionError,
            merge._merge, [0, 1, 2, 3, 4], 0, 2, 5)

    def testMerge_leftIndexIsSameAsMid_mergesArray(self):
        A = [5, 1, 2, -4, 0]
        merge._merge(A, 0, 0, 2)
        self.assertEquals(A, [1, 2, 5, -4, 0])

    def testMerge_indicesAreInMiddleOfA_mergesArray(self):
        A = [5, 1, 2, -4, 0]
        merge._merge(A, 1, 2, 3)
        self.assertEquals(A, [5, -4, 1, 2, 0])

    def testMerge_normalInput_mergesArray(self):
        A = [2, 4, 5, 7, 1, 2, 3, 6]
        merge._merge(A, 0, 3, 7)
        self.assertEquals(A, [1, 2, 2, 3, 4, 5, 6, 7])

    def testMergeSortHelper_givenMiddleIndices_sortsSubarray(self):
        A = [2, 4, 5, 7, 1, 2, 3, 6]
        merge._mergeSortHelper(A, 1, 5)
        self.assertEquals(A, [2, 1, 2, 4, 5, 7, 3, 6])

    def testMergeSortHelper_normalInput_sortsArray(self):
        A = CLRS_EXAMPLE
        merge._mergeSortHelper(A, 0, 7)
        self.assertEquals(A, CLRS_SORTED)

    def testMergeSort_normalInput_sortsArray(self):
        A = CLRS_EXAMPLE
        merge.mergeSort(A)
        self.assertEquals(A, CLRS_SORTED)

if __name__ == '__main__':
    unittest.main()