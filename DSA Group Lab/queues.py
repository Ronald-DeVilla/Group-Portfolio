class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_data

    def display(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def peek(self):
        if not self.front:
            return None
        return self.front.data