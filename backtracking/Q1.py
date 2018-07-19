# Subset
# Add to bookmarks (can be accessed from dashboard)
# Suggest edits in problem statement.
# Given a set of distinct integers, S, return all possible subsets.


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A, sort = True):
        if sort: A.sort()

        yield []
        for i in xrange(0, len(A)):
            for subset in self.subsets(A[i+1:], False):
                yield [A[i]] + subset