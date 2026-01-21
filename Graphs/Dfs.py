# Dfs for graphs
def dfs(node, result,visited, adj):
    visited[node] = 1
    result.append(node)
    for neighbor in adj[node]:
        if visited[neighbor] == 0:
            dfs(neighbor, result, visited, adj)

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

visited = [0] * (n + 1)
result = []
dfs(1, result, visited, adjencyList)
print(result)  # Output: [1, 2, 7, 6, 8, 3, 4, 5]

# TC O(N) + O(E) ~ O(N + E)
# N for nodes, E for edges
# SC O(N) + O(N) ~ O(N)
# N for visited array, N for recursion stack in worst case