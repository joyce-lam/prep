# Grid Unique Paths
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

# How many possible unique paths are there?

# Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
       
        A -=1;
        B-=1;
        num = A+B
        den = A
        res = 1
        for i in range(A):
            res *= (num-i)/(den-i)
        return int(round(res))