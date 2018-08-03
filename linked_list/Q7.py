# Remove Nth Node from List End
# Given a linked list, remove the nth node from the end of list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        
        list_length = 0
        
        temp = ListNode(None)
        temp.next = runner = A
        
        while runner != None:
            list_length += 1
            runner = runner.next
            
        if list_length == 1:
            return
        
        if B > list_length:
            return temp.next.next
        
        current = temp
        while list_length >= B:
            if list_length == B:
                current.next = current.next.next
                break

            else:
                current = current.next
                list_length -= 1
        return temp.next
        
