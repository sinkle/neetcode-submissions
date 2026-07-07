# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        h = {}
        i = 0
        node = head
        while node:
            h[i] = node
            i += 1
            node = node.next
        l = i

        i = 0
        node = new_head = ListNode()
        while i < l - 1 - i:
            node.next = h[i]
            node = node.next
            node.next = h[l - 1 - i]
            node = node.next
            i += 1
        if i == l - 1 - i:
            node.next = h[i]
            node = node.next
        node.next = None