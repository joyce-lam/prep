# Longest Substring Without Repeat
# Given a string, 
# find the length of the longest substring without repeating characters.
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):

		d = {}
		count = 0
		i = 0
		maxi = 0
		start = 0

		while i < len(A):
			if A[i] in d:
				if d[A[i]] >= start:
					count = i - start
					start = d[A[i]] + 1
					maxi = max(maxi, count)
			d[A[i]] = i
			i += 1

		maxi = max(maxi, i - start)
		return maxi
	
