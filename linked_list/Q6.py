# List Cycle
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

 
class Solution:
	# @param A : head node of linked list
	# @return the first node in the cycle in the linked list
	def detectCycle(self, A):
		slow_runner = A.next
		fast_runner = None
		if slow_runner:
			fast_runner = slow_runner.next
		while fast_runner and fast_runner != slow_runner:
			if fast_runner.next and fast_runner.next.next:
				slow_runner = slow_runner.next
				fast_runner = fast_runner.next.next
			else:
				fast_runner = fast_runner.next
		if fast_runner == slow_runner:
			slow_runner = A
			while fast_runner != slow_runner:
				slow_runner = slow_runner.next
				fast_runner = fast_runner.next
		return fast_runner