import collections
import queue
stack = collections.deque()
print(stack)
stack.append(10)
stack.append(20)
print(stack)
stack.pop()
print(stack)


stack1 = queue.LifoQueue()
stack1.put(1)
stack1.put(2)
stack1.put(3)
print(stack1)
print(stack1.get())
print(stack1.get())
print(stack1.get())


