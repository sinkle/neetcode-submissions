# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        rev = None
        node = head
        while node:
            if not rev:
                rev = ListNode(node.val)
            else:
                new_rev = ListNode(node.val, rev)
                rev = new_rev
                
            node = node.next

        return rev