class Queue:
    def __init__(self, head=None):
        if head:
            self.storage = [head]
        else:
            self.storage = []

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        if not self.storage:
            print "Queue is empty!"
            return
        else:
            return self.storage.pop(0)

# Setup
q = Queue()
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 2
print q.peek()

# Should be 2
print q.dequeue()

q.enqueue(4)
print q.dequeue()
print q.dequeue()
print q.dequeue()
q.enqueue(5)
print q.peek()
