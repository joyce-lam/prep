# Insertion Sort List
# Sort a linked list using insertion sort.






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        if not A.next:
            return A
        sorted_list = None
        def sortedinsert(node, sorted_list):
            if not sorted_list or sorted_list.val >= node.val:
                node.next = sorted_list
                sorted_list = node
            else:
                current = sorted_list
                while current.next is not None and current.next.val < node.val:
                    current = current.next
                node.next = current.next
                current.next = node
            
            return sorted_list
        
        current = A
        while current is not None:
            nxt = current.next
            sorted_list = sortedinsert(current, sorted_list)
            current = nxt
        
        return sorted_list
