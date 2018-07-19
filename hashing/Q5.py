# Substring Concatenation
# You are given a string, S, and a list of words, L, that are all of the same length.

# Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.



from collections import Counter

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        word_length = len(B[0])
        word_num = len(B)
        B = Counter(B)
        
        indices = []
        for index in range(len(A)):
            # check that first excerpt is a good match
            first_excerpt = A[index:index+word_length]
            if B.get(first_excerpt) is not None:
                # split potential substring by word length
                split = [A[i:i+word_length] for i in range(index, index+word_length*word_num, word_length)]
                if Counter(split) == B:
                    indices.append(index)
            
        return indices