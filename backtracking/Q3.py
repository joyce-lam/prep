# Permutations
# Given a collection of numbers, return all possible permutations.

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
	    res = []
	    l = 0
	    r = len(A) -1
	    def helper(a, l,r,res):
	        if l == r:
	            k = a[::]
	            res.append(k)
	        else:
	            for i in range(l,r+1):
	                a[l], a[i] = a[i], a[l]
	                helper(a, l+1,r, res)
	                a[l], a[i] = a[i], a[l]
	    helper(A,l,r,res)
	    return res