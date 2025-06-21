class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def __str__(self):
        return "front -> " + " | ".join(self.queue) + " <- rear"


queue = Queue()
queue.enqueue("Piter")
queue.enqueue("Polina")
queue.enqueue("Bobr")
queue.enqueue("Alesha")
queue.enqueue("Vasya")

print(queue)
print(queue.dequeue())

print(queue.peek())
print(queue.size())
