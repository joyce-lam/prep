# Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
# G[i] for an element A[i] = an element A[j] such that 
#     j is maximum possible AND 
#     j < i AND
#     A[j] < A[i]

class Solution:
    # @param A : list of integers
    # @return a list of integers
	def prevSmaller(A):
	    arr = []
	    ans = []

	    for i in range(len(A)):

	    	while len(arr) > 0 and arr[-1] >= A[i]:
	    		arr.pop()

	    	if len(arr) == 0:
	    		ans.append(-1)
	    	else:
	    		last = arr[-1]
	    		ans = append(last)
	    		

	    	arr.append(A[i])
	    return ans