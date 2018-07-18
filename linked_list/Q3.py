# Add Two Numbers as Lists
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        prev = None
        current = None
        head = None
        excess = 0
        while (A is not None or B is not None):
            if A is None:
                valA = 0
            else:
                valA = A.val
                
            if B is None:
                valB = 0
            else:
                valB = B.val
            
            sum_nodes = valA + valB + excess
            
            if sum_nodes < 10:
                new = ListNode(sum_nodes)
                excess = 0
            else:
                node_val = sum_nodes - 10
                new = ListNode(node_val)
                excess = 1
    
            if head is None:
                head = new
                
            else:
                current.next = new
                
            current = new
    
            if A is not None:
                A = A.next
    
            if B is not None:
                B = B.next
    
        if excess > 0:
            last_node = ListNode(excess)
            new.next = last_node
            
        return head