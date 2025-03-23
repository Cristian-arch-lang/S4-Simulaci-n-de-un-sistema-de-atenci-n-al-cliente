class Queue:
    class Node:
        def _init_(self, data):
            self.data = data
            self.next = None

    def _init_(self):
        self.front_node = None
        self.rear_node = None
        self._size = 0

    def enqueue(self, element):
        new_node = self.Node(element)
        if self.rear_node is None:
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        removed_data = self.front_node.data
        self.front_node = self.front_node.next
        if self.front_node is None:
            self.rear_node = None
        self._size -= 1
        return removed_data

    def front(self):
        return None if self.is_empty() else self.front_node.data

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size