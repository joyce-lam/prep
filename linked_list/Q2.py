# Swap List Nodes in pairs
# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        temp = A

        if temp is None:
            return  
        
        while(temp is not None and temp.next is not None):
            temp.val, temp.next.val = temp.next.val, temp.val
            temp = temp.next.next
        return A


