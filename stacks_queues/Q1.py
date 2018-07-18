# Redundant Braces
# Write a program to validate if the input string has redundant braces?
# Return 0/1

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
		stack = []

		for i in A:
			if i == ")":
				last = stack.pop()
				excess = 1
				while last is not "(":
					if last == "+" or last == "-" or last == "*" or last == "/":
						excess = 0

					last = stack.pop()

				if excess == 1:
					return 1
			else:
				stack.append(i)
