# Evaluate Expression
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):

		operators = {"+", "-", "*", "/"}
		nums = []
		
		for i in A:
			if i in operators:
				num2 = nums.pop()
				num1 = nums.pop()

				if i == "+":
					total = num1 + num2
				elif i == "-":
					total = num1 - num2
				elif i == "*":
					total = num1*num2
				elif i == "/":
					total = num1/num2

				nums.append(total)
			else:
				num = int(i)
				nums.append(num)

		return nums.pop()
