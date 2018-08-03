# Colorful Number
# For Given Number N find if its COLORFUL number or not

# Return 0/1
# A number can be broken into different contiguous sub-subsequence parts. 
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
# And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
class Solution:
    # @param A : integer
    # @return an integer
	def colorful(self, A):
	    A = str(A)
	    
	    main = []
	    list_main = []
	    for i in range(0, len(A)):
	        list_main.append(int(A[i]))

	    print("list_main", list_main)

	    for i in range(0, len(list_main)):
	        x = 1
	        for j in range(i, len(list_main)):

	            x *= list_main[j]
	            print("x", x)
	            
	            if x in main:
	                return 0
	            else:
	                main.append(x)
	                print("main1", main)
	    print("main2", main)
	    return 1

print(colorful(555))