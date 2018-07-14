# Palindrome Integer

# Determine whether an integer is a palindrome. Do this without extra space.

# A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
# Negative numbers are not palindromic.

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        def reverse(n):
            newnum=0
            while n>0:
                newnum = newnum*10 + n % 10
                n//=10
            return newnum
       
        if A == reverse(A):
            return 1
        else:
            return 0