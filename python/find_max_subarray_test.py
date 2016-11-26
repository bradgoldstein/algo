
# Tests for find_max_subarray.py
#
# Author: Bradley Goldstein

import find_max_subarray as fmcs

import unittest

# Example from CLRS 3rd ed. p.70
CLRS_EXAMPLE = [13, -3, -25, 20, -3, -16, -23, 18,
                20, -7, 12, -5, -22, 15, -4, 7]

class TestFindMaxSubarray(unittest.TestCase):

    def testFindMaxCrossingSubarray_smallArray_throws(self):
        self.assertRaises(AssertionError,
            fmcs._findMaxCrossingSubarray,[6], 0, 0, 0)

    def testFindMaxCrossingSubarray_unorderedIndices_throws(self):
        self.assertRaises(AssertionError,
            fmcs._findMaxCrossingSubarray,[1, 2, 4], 0, 2, 1)

    def testFindMaxCrossingSubarray_invalidLeftIndex_throws(self):
        self.assertRaises(AssertionError,
            fmcs._findMaxCrossingSubarray,[1, 2, 4], -1, 1, 2)

    def testFindMaxCrossingSubarray_invalidRightIndex_throws(self):
        self.assertRaises(AssertionError,
            fmcs._findMaxCrossingSubarray,[1, 2, 4], 0, 1, 4)

    def testFindMaxCrossingSubarray_midIsntInMiddle_performsAsExpected(self):
        self.assertEquals(
            fmcs._findMaxCrossingSubarray([-1, 1, 9, -100, 5, 6], 0, 1, 5),
            (1, 2, 10))

        self.assertEquals(
            fmcs._findMaxCrossingSubarray([-1, 1, 9, -100, 5, 6], 0, 4, 5),
            (4, 5, 11))

    def testFindMaxCrossingSubarray_normalInput_findsMaxCrossingSubarray(self):
        self.assertEquals(
            fmcs._findMaxCrossingSubarray([-1, 1, 9, -100, 5, 6], 0, 3, 5),
            (1, 5, -79))

    def testFindMaxSubarrayHelper_normalInput_findsMaxSubarray(self):
        self.assertEquals(
            fmcs._findMaxSubarrayHelper(CLRS_EXAMPLE, 0, 15),
            (7, 10, 43))

    def testFindMaxSubarray_normalInput_findsMaxSubarray(self):
        self.assertEquals(fmcs.findMaxSubarray(CLRS_EXAMPLE), (7, 10, 43))

if __name__ == '__main__':
    unittest.main()