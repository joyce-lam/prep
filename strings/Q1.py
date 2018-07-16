# Palindrome String
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


class Solution:
    # @param A : string
    # @return an integer
	def isPalindrome(self, A):
	    i = 0
	    j = len(A) - 1
 
	    while i < j:
	    	while i < j and not A[i].isalnum():
	    		i += 1
	    		
	    	while i < j and not A[j].isalnum():
	    		j -= 1
	    		
	    	if A[i].lower() != A[j].lower():
	    		return 0

	    	i, j = i + 1, j - 1

	    return 1
