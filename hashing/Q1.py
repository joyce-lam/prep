# 2 Sum
# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based. 

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        nums = {}
        ans = []
        for i in range(len(A)):
            number = A[i]
        
            diff = B - number
            if diff in nums:
                a = i + 1
                b = nums[diff] + 1
                return min(a, b), max(a, b)
            
            if number not in nums:
                nums[number] = i
        return ans