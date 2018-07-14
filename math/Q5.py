# Numbers of length N and value less than K
# Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.


from itertools import product
from itertools import ifilter
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if A == [] or B > len(str(C)):
            return 0
            
        elif B < len(str(C)):
            if B == 1:
                return len(A)
                
            else:
                candidates = product((str(i) for i in A), repeat = B)
                return sum(x[0] != '0' for x in candidates)
        elif B == len(str(C)):
        
            if B == 1:
                return sum(i < C for i in A)
            else:
                candidates = product((str(i) for i in A), repeat = B)
                return sum(x[0] != '0' and int(''.join(x)) < C for x in candidates)

                        