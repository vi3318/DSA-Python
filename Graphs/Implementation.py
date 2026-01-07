# Graphs 
# undirected graph and directed graphs 
# undirected edges and directed edges
# Cyclic graph is a graph starting and ending at the same vertex or node
# Path contains edges and vertices where all the nodes are reachable from each other
# Degree of a vertex is the number of edges connected to it
# Total degrees of a graph is equal to 2 times the number of edges
# indegree and outdegree are for directed graphs
# Weighted graph is a graph where edges have weights or costs associated with them

# Nodes and edges will be given 
# 0 index based graph or 1 index based graph

# using matrix to represent graph
# matrix[n+1][n+1] for 1 index based graph
n = 5
m = 6
edges= [[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]
# 1 based index graph 
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
print(matrix)

for u,v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1  # undirected graph
print(matrix)
'''
[
 [0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 0, 0],
 [0, 1, 0, 0, 1, 0],
 [0, 1, 0, 0, 1, 1],
 [0, 0, 1, 1, 0, 1],
 [0, 0, 0, 1, 1, 0]
]
'''

# using adjacency list to represent graph
lst = [[] for _ in range(n+1)]
for u,v in edges:
    lst[u].append(v)
    lst[v].append(u)  # undirected graph
print(lst)

# Dictionary approach 
myDictionary = {}
for i in range(1,n+1):
    myDictionary[i] =[]

for u,v in edges:
    myDictionary[u].append(v)
    myDictionary[v].append(u)  # undirected graph
print(myDictionary)