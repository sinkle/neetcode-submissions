# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h = []
        while head:
            if id(head) not in h:
                h.append(id(head))
                head = head.next
            else:
                return True
        
        return False