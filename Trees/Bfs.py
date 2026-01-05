# Breadth First Search (BFS) implementation for tree traversal
from collections import deque

def levelOrdeTraversal(node):
    result = []
    queue = deque([])
    queue.append(node)
    while len(queue) != 0:
        e = queue.popleft()
        result.append(e.val)
        if e.left != None:
            queue.append(e.left)
        if e.right != None:
            queue.append(e.right)
    return result

# TC O(N)
# SC O(N)
