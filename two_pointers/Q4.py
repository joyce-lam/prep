# Remove Duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
		if len(A) == 0:
			return 0

		i = 0

		for j in range(1, len(A)):
			print(len(A))
			if A[i] != A[j]:
				i += 1
				A[i] = A[j]
		return i + 1
