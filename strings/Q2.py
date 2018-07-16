# Minimum Characters required to make a String Palindromic
# You are given a string. The only operation allowed is to insert characters in the beginning of the string. How many minimum characters are needed to be inserted to make the string a palindrome string


class Solution:
    # @param A : string
    # @return an integer
	def solve(self, A):
	    n = len(A)
	    if not n:
	        return ''
	    rev, i = A[::-1], 0
	    for j in range(1, n+1):
	        if rev[-j:] == A[:j]:
	            i = j
	    
	    par = rev[:n-i]+A
	    
	    return len(par) - len(A)


