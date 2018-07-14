# Set Matrix Zeros
# Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

# Do it in place.

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        row_flag = False
        col_flag = False
        
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if (i == 0 and A[i][j] == 0):
                    row_flag = True
                    
                if (j == 0 and A[i][j] == 0):
                    col_flag = True
                
                if (A[i][j] == 0):
                    A[0][j] = 0
                    A[i][0] = 0
                    
        
        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                if (A[0][j] == 0 or A[i][0] == 0):
                    A[i][j] = 0
        
        if (row_flag == True):
            for i in range(0, len(A[0])):
                A[0][i] = 0
                
        
        if (col_flag == True):
            for i in range(0, len(A)):
                A[i][0] = 0
                
        return A