# Minimize the absolute difference
# Given three sorted arrays A, B and Cof not necessarily same sizes.

# Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
# i.e. minimize | max(a,b,c) - min(a,b,c) |.
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
		a = len(A)
		b = len(B)
		c = len(C)

		i = 0
		j = 0
		k = 0

		diff = max(A[i], B[j], C[k]) - min(A[i], B[j], C[k])
		
		while i < a and j < b and k < c:
			minimum = min(A[i], B[j], C[k])
			maximum = max(A[i], B[j], C[k])

			current_diff = maximum - minimum

			if current_diff < diff:
				diff = maximum - minimum
			
			if diff == 0:
				break

			if A[i] == minimum:
				i += 1
			elif B[j] == minimum:
				j += 1
			else:
				k += 1
	
		return diff

