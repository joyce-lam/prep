# Reverse the string
# Given an input string, reverse the string word by word.

# Example:

# Given s = "the sky is blue",

# return "blue is sky the".


class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):

        if len(A) == 1:
            return A
            
        words = A.split()
        sentence_rev = " ".join(reversed(words))
        
        return sentence_rev
