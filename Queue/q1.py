class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None

    def size(self):
        return len(self.items)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue size:", queue.size())  
print("Front element:", queue.peek()) 
print("Dequeued element:", queue.dequeue())
print("Queue size after dequeue:", queue.size())