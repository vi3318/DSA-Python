# Dequeue
# Double ended queue implementation
# inserting and popping from both ends is O(1) time complexity
from collections import deque

list = deque([])

deque.append(10)        # insert at the end
deque.append(20)
deque.appendleft(5)    # insert at the beginning
print(deque)            # deque([5, 10, 20])
