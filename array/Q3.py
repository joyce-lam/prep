# Find Duplicate in Array
# Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.
# If there are multiple possible answers ( like in the sample case above ), output any one.
# If there is no duplicate, output -1

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
      
        s = sum(A)
        n = len(A)
        missing = s - (n*(n-1))/2
        return missing