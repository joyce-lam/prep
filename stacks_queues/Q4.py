# Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.


class MinStack:
    def __init__(self):
    	self.min = None
    	self.stack = []
    	self.minStack = []

    # @param x, an integer
    def push(self, x):
    	if self.stack is None:
    		self.stack.append(x)
    		self.min = x
    		self.minStack.append(x)
    	else:
    		self.stack.append(x)
    		if x < self.min:
    			self.min = x
    			self.minStack.append(x)

    # @return nothing
    def pop(self):
    	if len(self.stack) == 0:
    		return
    	else:
	    	out = self.stack.pop()
	    	if out == self.min:
	    		self.minStack.pop()


    # @return an integer
    def top(self):
    	if len(self.stack) == 0:
    		return -1
    	else:
	    	last = self.stack[-1]
	    	return last
	  

    # @return an integer
    def getMin(self):
    	if len(self.stack) == 0:
    		return -1
    	else:
    		return self.min