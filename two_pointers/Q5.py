# Array 3 Pointers
# Find i, j, k such that :
# max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
# Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

# **abs(x) is absolute value of x and is implemented in the following manner : **

      # if (x < 0) return -x;
      # else return x;
import sys
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):


		a = len(A)
		b = len(B)
		c = len(C)

		i = 0
		j = 0
		k = 0

		diff = sys.maxint
		while i < a and j < b and k < c:
			minimum = min(A[i], B[j], C[k])
			maximum = max(A[i], B[j], C[k])

			current_diff = maximum - minimum

			if current_diff < diff:
				res_i = i
	        	res_j = j
	        	res_k = k
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