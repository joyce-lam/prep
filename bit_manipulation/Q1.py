# Min XOR value
# Given an array of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.


# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def findMinXor(self, seq):
#         seq.sort()
#         min_xor = seq[0] ^ seq[1]
#         # min is always achieved by two neighbours in sorted array
#         for i in xrange(len(seq) - 1):
#             min_xor = min(min_xor, seq[i] ^ seq[i+1])
#         return min_xor


def findMinXor(seq):
    seq.sort()
    min_xor = seq[0] ^ seq[1]
    print(min_xor)
    # min is always achieved by two neighbours in sorted array
    for i in xrange(len(seq) - 1):
    	print(seq[i] ^ seq[i+1])
        min_xor = min(min_xor, seq[i] ^ seq[i+1])
        print("2", min_xor)
    return min_xor
	
seq = [0, 2, 5,7, 9, 11]
findMinXor(seq)