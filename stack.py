class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_emtpy():
            return None
        
        return self.stack.pop()
    
    def is_emtpy(self):
        return len(self.stack) == 0
    
    def peek(self):
        if self.is_emtpy():
            return None
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def __str__(self):
        return "bottom " + " | ".join(map(str, self.stack)) + " top"

# bottom ... | ... | top
stack = Stack()
stack.push('Python')
stack.push('Go')
stack.push("C++")

print(stack)

print('Top element: ', stack.peek())
print('Delete: ', stack.pop())

print('Top element: ', stack.peek())
print('Size of stack: ', stack.size())
print('Stack is empty: ', stack.is_emtpy())