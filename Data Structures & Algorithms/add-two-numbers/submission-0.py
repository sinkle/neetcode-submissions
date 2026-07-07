# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add = 0
        node = head = ListNode()

        while l1 or l2:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            v = d1 + d2 + add
            add = 0
            if v > 9:
                add = 1
                v = v - 10
            node.next = ListNode(v)
            node = node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if add:
            node.next = ListNode(add)
        
        return head.next


