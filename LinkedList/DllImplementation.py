# Doubly linked list implementation
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
class DllNode:
    def __init__(self):
        self.head = None
       
    
    def insertAtHead(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev= new_node
            self.head = new_node
            # TC O(1)
            # SC O(1)
    
    def append(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            # TC O(N)
            # SC O(1)
    def insertBetween(self,val,pos):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current and count < pos:
                current = current.next
                count += 1
            if current:
                new_node.prev = current.prev
                new_node.next = current
                if current.prev:
                    current.prev.next = new_node
                current.prev = new_node
                if pos == 0:
                    self.head = new_node
            # TC O(N)
            # SC O(1)
    def display(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()
        # TC O(N)
        # SC O(1)
    def deleteHead(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
        # TC O(1)
        # SC O(1)
    def deleteTail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next:
                current = current.next
            current.prev.next = None
        # TC O(N)
        # SC O(1)
        def deleteAtPosition(self,pos):
            if not self.head:
                return
            if pos == 0:
                self.deleteHead()
                return
            current = self.head
            count = 0
            while current and count < pos:
                current = current.next
                count += 1
            if current:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next


    

dll = DllNode()
dll.insertAtHead(10)
