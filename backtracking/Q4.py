# Kth Permutation Sequence
# The set [1,2,3,…,n] contains a total of n! unique permutations.
# Given n and k, return the kth permutation sequence.

class Solution::
         # @param n : integer# @param n  
    # @param k : integer
    # @return a strings
    def getPermutation(self, n, k):
        k -= 1
        sums = 1
        ans = ''
        factorial = [1]
        for i in range(1 , n):
            sums *= i
            factorial.append(sums)
        
        nums = []
        for i in range( 1, n+1):
            nums.append(i)
        
        for i in range(1 , n+1):
            index = k/factorial[n-i]
            ans += str(nums[index])
            nums = nums[:index] + nums[index+1:]
            k = k - index*factorial[n-i]
        
        return ans