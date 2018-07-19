# Anagrams
# Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):

		anagrams = {}
		for i in xrange(len(A)):
			key = ''.join(sorted(A[i]))
			if key in anagrams:
				anagrams[key].append(i+1)
			else:
				anagrams[key] = [i+1]
		for key in anagrams:
			if len(anagrams[key]) < 1:
				del anagrams[key]
		return [ i for i in anagrams.itervalues()]


