# Pascal Triangle
# Given numRows, generate the first numRows of Pascal’s triangle.
# Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
# Example:
# Given numRows = 5,
# Return
# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]
class Solution:
	def generate(self, A):
        if A <= 0:
            return []
        result = [[1]]
        for r in range(1, A):
            row = [1]
            for i in range(1,r):
                row.append(result[r-1][i-1] + result[r-1][i])
            row.append(1)
            result.append(row)
        return result

