# Bfs on one based index graph
from collections import deque

def bfs(n,adj,startingNode):
    ans = []
    queue = deque()
    visited = [0] * (n+1)
    queue.append(startingNode)
    visited[startingNode] = 1
    while len(queue) != 0:
        e = queue.popleft()
        ans.append(e)
        for node in adj[e]:
            if visited[node] == 0:
                visited[node] = 1
                queue.append(node)

    return ans

n = 9
adjencyList = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3],
    [3],
    [7],
    [2, 6, 8],
    [1, 7],
    []
]

print(bfs(n, adjencyList, 1))  # Output: [1, 2, 3, 8, 7, 4, 5, 6]

# TC O(N) + O(E) ~ O(N + E)
# N for nodes, E for edges
# SC O(N) + O(N) + O(N) ~ O(N)
# N for ans array, N for visited array, N for queue in worst case