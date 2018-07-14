# FizzBuzz
# Given a positive integer N, print all the integers from 1 to N. But for multiples of 3 print “Fizz” instead of the number and for the multiples of 5 print “Buzz”. Also for number which are multiple of 3 and 5, prints “FizzBuzz”.

class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        num_array = []
        for num in range(1, len(A) + 1):
            if num % 3 == 0 and num % 5 == 0:
                num_array.append("FizzBuzz")
            elif num % 3 == 0:
                num_array.append("Fizz")
            elif num % 5 ==0:
                num_array.append("Buzz")
            else:
                num_array.append(str(num))
        return num_array