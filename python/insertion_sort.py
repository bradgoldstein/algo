
# Insertion Sort sorting alogrithm
#
# See p.16-22 in CLRS 3rd ed.
#
# Author: Bradley Goldstein


# Sorts the list inplace.
#
# Args:
#	A: list of values to be sorted
def insertionSort(A):
	for j in range(1, len(A)):
		key = A[j]
		# Insert A[j] into the sorted sequence A[1...j-1]
		i = j - 1
		while (i >= 0 and  A[i] > key):
			A[i + 1] = A[i]
			i -= 1
		A[i + 1] = key

