# 1)Снять верхушку стека без удаления
#  Вывести верхний элемент, но не удалять его.
#  Пример: стек ["a", "b", "c"] → выведет "c"

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

    def clear(self):
        self.stack.clear()

    def __iter__(self):
        return iter(self.stack)
    
    def __str__(self):
        return "bottom " + " | ".join(map(str, self.stack)) + " top"


stack1 = Stack()
stack1.push("a")
stack1.push("b")
stack1.push("c")

print('Верхний элемент: ', stack1.peek())


#  2. Сколько элементов в стеке
#  Посчитать количество элементов, добавленных в стек
#  Пример: после push('a'), push('b') → ответ: 2

stack2 = Stack()

stack2.push("a")
stack2.push("b")

print('Количество элементов: ', stack2.size())


#  3. Очистка стека
#  Удалить все элементы из стека

stack1.clear()

# 4. Сумма всех чисел
#  Посчитать сумму всех чисел в списке
#  Пример: [1, 2, 3] → 6

stack3 = Stack()

stack3.push(1)
stack3.push(2)
stack3.push(3)

total = 0
for item in stack3:
    total += item

print("Сумма всех чисел:", total)


#  5. Поиск элемента
#  Найти, есть ли заданное число в списке
#  Пример: [1, 2, 3] и число 2 → верно
def contains(stack, target):
    for item in stack:
        if item == target:
            return True
    return False

stack5 = Stack()
stack5.push(1)
stack5.push(2)
stack5.push(3)

target = 2
print(f"Число {target} найдено:", contains(stack5, target))  # → True


#  6. Подсчёт количества чётных
#  Посчитать, сколько в списке чётных чисел
#  Пример: [2, 3, 4] → 2

def count_even(stack):
    count = 0
    for item in stack:
        if isinstance(item, int) and item % 2 == 0:
            count += 1
    return count

stack6 = Stack()
stack6.push(2)
stack6.push(3)
stack6.push(4)

print("Количество чётных чисел:", count_even(stack6))  # → 2


#  7. Добавить и обслужить одного клиента
#  Добавить в очередь имя, а потом сразу его обслужить

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


q7 = Queue()
q7.enqueue("Олег")
served = q7.dequeue()

print("Обслужен клиент:", served)  # → Олег



#  8 Вывести текущую очередь
#  Напечатать все элементы в порядке поступления
#  Пример: ["Маша", "Петя"] → "Маша → Петя

q8 = Queue()
q8.enqueue("Маша")
q8.enqueue("Петя")

print("Текущая очередь:", q8)
