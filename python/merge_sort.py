
# Merge Sort sorting alogrithm
#
# See p.30-37 in CLRS 3rd ed.
#
# Author: Bradley Goldstein


# Merges two contiguous, sorted sublists, A[p...q] and A[q+1...r] so that
# A[p...r] is now sorted. Uses temporary arrays of size O(len(A)).
#
# Args:
#	A: a list containing values to be merged
#	p: start index of first list subset to be merged
#	q: end index of first list subset to be merged
#	r: end index of second list subset to be merged
def _merge(A, p, q, r):
	assert 0 <= p <= q < r < len(A), 'Array indices are out of order.'

	L = A[p:q+1]
	L.append(float('inf'))

	R = A[q+1:r+1]
	R.append(float('inf'))

	i, j = 0, 0
	for k in range(p, r + 1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1


# Sorts the list between the given indices.
#
# Args:
#	A: list of values to be sorted
#	p: start index of sublist to be sorted
#	r: end index of sublist to be sorted
def _mergeSortHelper(A, p, r):
	if p < r:
		q = (p + r) / 2
		_mergeSortHelper(A, p, q)
		_mergeSortHelper(A, q + 1, r)
		_merge(A, p, q, r)


# Sorts the list.
#
# Args:
#	A: list of values to be sorted
def mergeSort(A):
	_mergeSortHelper(A, 0, len(A) - 1)

