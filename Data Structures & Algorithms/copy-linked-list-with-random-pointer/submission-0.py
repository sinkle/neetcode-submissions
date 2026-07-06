"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_node = new_head = Node(0)
        node = head
        
        m = {}

        while node:
            new_node.next = Node(0)
            new_node = new_node.next

            m[id(node)] = new_node

            new_node.val = node.val
            node = node.next
        
        new_head = new_head.next
        new_node = new_head

        while head:
            if head.random:
                new_node.random = m[id(head.random)]

            head = head.next
            new_node = new_node.next
        
        return new_head




            