# Single Number
# Given an array of integers, every element appears twice except for one. Find that single one.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        dict = {}

        for i in A:
            if i in dict:
                dict[i] += 1
            else: 
                dict[i] = 1

        for k in dict:
            if dict[k] == 1:
                return k
                
        return None