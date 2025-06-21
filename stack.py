# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if self.is_empty():
#             return None
#         return self.stack.pop()
#
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def peek(self):
#         if self.is_empty():
#             return None
#         return self.stack[-1]
#
#     def size(self):
#         return len(self.stack)
#
#     def __str__(self):
#         return "bottom " + ' | '.join(map(str, self.stack)) + " top"

# stack = Stack()
# stack.push('Python')
# stack.push('Go')
# stack.push("Rust")
# stack.push('C++')
#
# print(stack)
# print("Top Node" , stack.peek())
# print('Del' , stack.pop())
#
# print("Top Node" , stack.peek())
# print('Size' , stack.size())
# print("Stack is empty", stack.is_empty())

# s = "hello"
# def reverse_stack(s):
#     stack = []
#     res = ""
#     for symbol in s:
#         stack.append(symbol)
#
#     while stack:
#         res += stack.pop()
#
#     return res
#
#
# print(reverse_stack(s))

# pairs = {
#     '(': ')',
#     '{': '}',
#     '[': ']'
# }
#
# s = '{([])}'
# s = '[({])}'
# s = '[({'
# def balance(s):
#     stack = []
#     for sym in s:
#         if sym in '[{(':
#             stack.append(sym)
#         elif sym in ']})':
#             if not stack:
#                 return False
#             last = stack.pop()
#             if pairs[last] != sym:
#                 return False
#
#             # if pairs[sym] == stack[-1]:
#             #     stack.pop()
#
#     return not stack
#
# print( balance(s) )


# def not_dublicate(s):
#     stack = []
#     for char in s:
#         # if stack and char != stack[-1]:
#         #     stack.append(char)
#         # else:
#         #     stack.pop()
#
#
#         if char not in stack:
#             stack.append(char)
#         else:
#             stack.pop()
#     return ''.join(stack)
#
# print(not_dublicate('abbaca'))

def polyndrome(s):
    stack = []
    n = len(s)

    for i in range(n // 2):
        stack.append(s[i])

    start = n // 2
    if n % 2 != 0:
        start += 1

    for i in range(start, n):
        if not stack or s[i] != stack.pop():
            return False

    return True


# print(polyndrome('level'))
print(polyndrome('madam'))

