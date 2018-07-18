# Remove Duplicates from Sorted List
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
    	if A is None:
            return A
            
        node = A
        
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next 
        return A