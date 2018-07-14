# Max Sum Contiguous Subarray
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example:

# Given the array [-2,1,-3,4,-1,2,1,-5,4],

# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# For this problem, return the maximum sum.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
       
        ans = 0
        sum_so_far = 0
        neg = 0
        
        for i in range(len(A)):
            if A[i] < 0:
                neg += 1
            if (sum_so_far + A[i] > 0):
                sum_so_far += A[i]
            else:
                sum_so_far = 0
            ans = max(sum_so_far, ans)
            
            if neg == len(A):
                return max(A)
        return ans