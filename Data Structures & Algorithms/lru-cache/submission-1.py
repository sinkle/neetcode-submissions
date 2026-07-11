class Node:
    def __init__(self, val=0, key=0, next_=None, prev=None):
        self.val = val
        self.next_ = next_
        self.prev = prev
        self._key = key


class LRUCache:

    _cap = 0
    _curr_cap = 0

    _c: dict | None = None

    _head = None 
    _tail = None


    def __init__(self, capacity: int):
        self._cap = capacity
        self._c = {}

    def _remove_node(self, node: Node):
        if self._curr_cap == 1:
            self._head = None
            self._tail = None
        elif not node.next_:
            self._tail = self._tail.prev
            self._tail.next_ = None
        elif not node.prev:
            self._head = node.next_
            self._head.prev = None
        else:
            node.prev.next_ = node.next_
            node.next_.prev = node.prev
            
    def _add_tail(self, node):
        if not self._tail:
            return self._init_ll
            
        node.next_ = None
        self._tail.next_ = node
        node.prev = self._tail
        self._tail = self._tail.next_

    def _init_ll(self, node):
        self._head = self._tail = node 
    

    def get(self, key: int) -> int:
        node = self._c.get(key)
        if not node:
            return -1

        if self._curr_cap == 1:
            return node.val

        self._remove_node(node)
        self._add_tail(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        node = Node(value, key)
        
        if self._curr_cap == 0:
            self._init_ll(node)
            self._c[key] = node
            self._curr_cap = 1
            return

        if key not in self._c:
            if self._cap > self._curr_cap:
                self._add_tail(node)
                self._c[key] = node
                self._curr_cap += 1
            else:
                self._c.pop(self._head._key)
                self._remove_node(self._head)
                self._add_tail(node)
                self._c[key] = node
        else:
            prev_node = self._c[key]
            self._remove_node(prev_node)
            self._add_tail(node)
            self._c[key] = node



        

        
