class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()


    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return "bottom " + ' | '.join(map(str, self.stack)) + " top"

stack = Stack()
stack.push('Python')
stack.push('Go')
stack.push("Rust")
stack.push('C++')

print(stack)
print("Top Node" , stack.peek())
print('Del' , stack.pop())

print("Top Node" , stack.peek())
print('Size' , stack.size())
print("Stack is empty", stack.is_empty())