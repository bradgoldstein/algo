
# Tests for insertion_sort.py
#
# Author: Bradley Goldstein

import insertion_sort as sort

import unittest


class TestInsertionSort(unittest.TestCase):

    def testInsertionSort_emptyArray_isNoop(self):
        A = []
        sort.insertionSort(A)
        self.assertEquals(A, list())

    def testInsertionSort_sizeOnearray_isNoop(self):
        A = [42]
        sort.insertionSort(A)
        self.assertEquals(A, [42])

    def testInsertionSort_integerInput_sorts(self):
        A = [5, 2, 4, 6, 1, 3]  # Example from CLRS p.18 3rd ed.
        sort.insertionSort(A)
        self.assertEquals(A, [1, 2, 3, 4, 5, 6])

    def testInsertionSort_stringInput_sorts(self):
        A = ['e', 'b', 'd', 'f', 'a', 'c'] 
        sort.insertionSort(A)
        self.assertEquals(A, ['a', 'b', 'c', 'd', 'e', 'f'])

    def testInsertionSort_repeatedValues_sorts(self):
        A = [2, 3, 4, 3, 2, 3, 1]  # Example from CLRS p.18 3rd ed.
        sort.insertionSort(A)
        self.assertEquals(A, [1, 2, 2, 3, 3, 3, 4])

if __name__ == '__main__':
    unittest.main()