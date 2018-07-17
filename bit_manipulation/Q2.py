# Number of 1 Bits
# Write a function that takes an unsigned integer and returns the number of 1 bits it has.

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
		binary_num = bin(A)[2:]
		binary_num = str(binary_num)
		count = 0
		for i in range(0, len(binary_num)):
			if binary_num[i] == "1":
				count += 1
		return count