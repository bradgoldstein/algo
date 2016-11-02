
#
# Algorithm to find the subarray with the greatest sum of any contiguous
# subarray in array A.
#
# See 70-74 in CLRS 3rd ed.
#

# Args:
#	A: A list of comparable values
#	low: first index in A
#	mid: mid index in A
#	high: last index in A
# Returns:
#	A tuple containing the indices of the greatest subarray that crosses the
#	midpoint, and the sum of the values in that array:
# 		(left, right, sum) where,
# 	low <= left <= mid and
#	mid <= right <= high.
def findMaxCrossingSubarray(A, low, mid, high):
	assert len(A) > 1, 'Array A must have > 2 elements but has %d.' % len(A)
	assert 0 <= low <= mid <= high <= len(A), 'Array indices are out of order.'

	# Find max sum to the left of mid ending at mid
	left_sum = float('-inf')
	total_sum = 0
	max_left = mid
	for i in reversed(range(low, mid + 1)):
		total_sum += A[i]
		if total_sum > left_sum:
			left_sum = total_sum
			max_left = i
	
	# Find max sum to the right of mid + 1 starting at mid + 1
	right_sum = float('-inf')
	total_sum = 0
	max_right = mid + 1
	for i in range(mid + 1, high + 1):
		total_sum += A[i]
		if total_sum > right_sum:
			right_sum = total_sum
			max_right = i

	return (max_left, max_right, left_sum + right_sum)

# Args:
#	A: A list of comparable values
#	low: first index in A
#	high: last index in A
# Returns:
#	A tuple containing the indices of the greatest subarray,
#	and the sum of the values in that array:
# 		(left, right, sum) where,
# 	left <= right.
def findMaxSubarrayHelper(A, low, high):
	if low == high:  # base case
		return (low, high, A[low])

	mid = (low + high) / 2
	left_low, left_high, left_sum = findMaxSubarrayHelper(A, low, mid)
	right_low, right_high, right_sum = findMaxSubarrayHelper(A, mid + 1, high)
	cross_low, cross_high, cross_sum = findMaxCrossingSubarray(
		A, low, mid, high)

	max_sum = max(left_sum, right_sum, cross_sum)
	if max_sum == left_sum:
		return (left_low, left_high, left_sum)
	if max_sum == right_sum:
		return (right_low, right_high, right_sum)
	if max_sum	== cross_sum:
		return (cross_low, cross_high, cross_sum)

	raise ValueError

def findMaxSubarray(A):
	return findMaxSubarrayHelper(A, 0, len(A) - 1)

