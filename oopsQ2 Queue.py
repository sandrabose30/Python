
# Data Structures
# Stack = LILO
# queue = FIFO
# enqueue(7)
# dequeue()
# []
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop()
q1=Queue()
q1.enqueue(1)
q1.enqueue("mohan")
q1.enqueue(3)
q1.enqueue(2)
print(q1.items)
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.items)