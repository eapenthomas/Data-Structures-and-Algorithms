import queue
import collections

que = collections.deque()  # Using deque from collections module
q = queue.Queue()          # Using Queue from the queue module

# Putting an item in the queue
q.put(10)
q.put(0)
q.put(20)
q.put(30)
print(q.get())
print(q.get())
print(q.get())
print(q.get())



#insertion and deletion from same side
que.appendleft(10)
que.appendleft(20)
que.appendleft(30)
print("Queue : ",que)
que.popleft()
print("Queue : ",que)
que.popleft()
print("Queue : ",que)

#insertion from one side and deletion from ather side
que.append(10)
