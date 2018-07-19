# Generate all Parentheses II
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
		ans = []

		def helper(a, left, right):
			if len(a) == 2 * A:
				ans.append(a)
				return

			if left < A:
				helper(a + "(", left + 1, right)
			if right < left:
				helper(a + ")", left, right + 1)


		helper("", 0, 0)
		return ans
