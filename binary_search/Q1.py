# Square Root of Integer
# Implement int sqrt(int x).

# Compute and return the square root of x.

# If x is not a perfect square, return floor(sqrt(x))



class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if (A == 0 or A == 1):
            return A
            
        start = 1
        end = A
        
        while start <= end:
            mid = (start + end) /2
            
            if (mid * mid == A) : 
                return mid
                
            elif (mid * mid < A):
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans