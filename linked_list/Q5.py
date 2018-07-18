# Reorder List
# Given a singly linked list
# L: L0 → L1 → … → Ln-1 → Ln,
# reorder it to:
# L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        if A is None or A.next is None:
            return A
        slow = A
        fast = A
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next
        slow.next = None

        last = None
        while right:
            curr = right
            right = right.next
            curr.next = last
            last = curr
        temp = ListNode(0)
        tail = temp
        
        while A or last:
            if A:
                tail.next = A
                tail = A
                A = A.next
            if last:
                tail.next = last
                tail = last
                last = last.next
        tail.next = None
        return temp.next





