#sort list
#Sort a linked list in O(n log n) time using constant space complexity.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):

    	def getMiddle(head):
    		slow = head
    		fast = head.next

    		while fast is not None:
    			fast = fast.next
    			if fast is not None:
    				fast = fast.next
    				slow = slow.next
    		return slow

    	def mergeTwoLists(A,B):
    		head = ListNode(0)
    		p = head

    		while A or B:
    			if A and B:
    				if A.val < B.val:
    					p.next = A
    					A = A.next

    				else:
    					p.next = B
    					B = B.next

    				p = p.next

    			if A == None:
    				p.next = B
    				break
    			elif B == None:
    				p.next = A
    				break
    		return head.next

    	def sortlist(A):
    		if not A.next:
    			return A
    		mid = getMiddle(A)
    		next_of_mid = mid.next

    		mid.next = None

    		left = sortlist(A)
    		right = sortlist(next_of_mid)

    		sortedList = mergeTwoLists(left, right)
    		return sortedList

    	return sortlist(A)
