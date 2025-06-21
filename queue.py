class Queue:
    def __init__(self):
        self.queue = []
    
    #добавление элемента в конец очереди
    def enqueue(self, item):
        self.queue.append(item)
    
    #удалить и вернуть элемент из начала очереди
    def dequeue(self):
        if self.is_emtpy():
            return None
        return self.queue.pop(0)
    
    #is empty
    def is_emtpy(self):
        return len(self.queue) == 0
    
    #peek
    def peek(self):
        if self.is_emtpy():
            return None 
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return "front -> " + " | ".join(self.queue) + " <- rear"

# front -> .... | .... <- rear

q = Queue()

q.enqueue('A')
q.enqueue('B')

print(q)