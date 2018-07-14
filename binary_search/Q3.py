# Implement Power Function
# Implement pow(x, n) % d.

# In other words, given x, n and d,

# find (xn % d)

# Note that remainders on division cannot be negative. 
# In other words, make sure the answer you return is non negative.


class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        
        ans = 1
        if (x == 0):
            return 0

        if (n == 0):
            return 1
        x = x % d
    
        while (n > 0):
    
            if ((n & 1) == 1):
                ans = ans * x % d
    
            n = n >> 1
            x = (x * x) % d
        return ans