# 3 Sum
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
		A.sort()
		result = 0
		min = A[0]
		for i in range(0, len(A)):
			if min < A[i]:
				min = A[i] 

		for i in range(0, len(A)):
			next = i + 1
			last = len(A) - 1

			while next < last:
				sum = A[i] + A[next] + A[last]
				
				if A[i] < 0 and A[next]< 0 and A[last] < 0:
					diff = sum - B
				else:
					diff = abs(sum - B)

				if (diff == 0):
					return sum

				if (diff < min):
					min = diff
					result = sum

				if (sum <= B):
					next += 1
				else:
					last -= 1

		return result
