# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        d = {}
        c = 0
        node = head
        while node:
            d[c] = node
            node = node.next
            c += 1
        
        if n == c:
            return d[1]
        elif n == 1:
            if n := d.get(c-2):
                n.next = None
                return head
            else:
                return None
        else:

            d[c - n - 1].next = d.get(c - n + 1)

        return head

