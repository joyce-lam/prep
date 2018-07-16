# Justified Text
# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

# Pad extra spaces  when necessary so that each line has exactly L characters.
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left justified and no extra space is inserted between words.

# Your program should return a list of strings, where each string represents a single line.

# Example:

# words: ["This", "is", "an", "example", "of", "text", "justification."]

# L: 16.

# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
		ans = []
		current_line = []
		char = 0

		if len(A) == 0:
	        return ans

		for word in A:
			l = char + len(word) + len(current_line)

			if l > B:
				for i in range(B - char):
					current_line[i % (len(current_line) - 1 or 1)] += " "
				ans.append("".join(current_line))
				current_line = []
				char = 0
			current_line += [word]
			char += len(word)

		return ans + [" ".join(current_line).ljust(B)]
