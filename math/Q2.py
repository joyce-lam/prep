# Excel Column Number
# Given a column title as appears in an Excel sheet, return its corresponding column number.


class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        multiplier = 1
        result = 0
        for char in reversed(A):
            result += (ord(char) - ord('A') + 1) * multiplier
            multiplier *= 26
        return result