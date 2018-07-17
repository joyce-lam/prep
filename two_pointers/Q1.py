# Intersection Of Sorted Arrays
# Find the intersection of two sorted arrays.
# OR in other words,
# Given 2 sorted arrays, find all the elements which occur in both the arrays.

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        numdict = {}
        intersection = []
        
        for i in range(len(A)):
            num = A[i]
            
            if num in numdict:
                numdict[num] += 1
            else:
                numdict[num] = 1
            
        for j in B:
            if j in numdict and numdict[j] > 0:
                numdict[j] -= 1
                intersection.append(j)
        return intersection