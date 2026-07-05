# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        node1, node2 = list1, list2
        res = None
        while True:
            if node1 and node2:
                if node1.val < node2.val:
                    new = node1
                    node1 = node1.next
                else:
                    new = node2
                    node2 = node2.next
            elif node1:
                new = node1
                node1 = node1.next
            else:
                new = node2
                node2 = node2.next
            
            if res is None:
                res = new
                head = new
            else:
                res.next = new
                res = res.next
            
            if not (node1 or node2):
                break
        
        return head

        
