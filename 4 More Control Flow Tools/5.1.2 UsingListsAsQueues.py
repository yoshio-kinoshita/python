from collections import deque
queue = deque(["Eric", "Jhon", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)