# Roman To Integer
# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

# I V X L C D M
# 1 5 10 50 100 500 1000

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
		d = {
			"I": 1,
			"V": 5,
			"X": 10,
			"L": 50,
			"C": 100,
			"D": 500,
			"M": 1000
		}

		ans = 0
		i = 0

		while (i < len(A)):
			num1 = d[A[i]]

			if (i + 1 < len(A)):
				num2 = d[A[i+1]]

				if num1 >= num2:
					ans += num1
					i += 1
				else:
					ans = ans + num2 - num1
					i = i + 2
			else:
				ans += num1
				i += 1
		return ans
