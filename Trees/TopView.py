# Top view of a binary tree
# -2,-1,0,1,2
# first node on imaginary line 
from collections import deque
def topView(root):
    if root is None:
        return 
    ans=[]
    queue=deque()
    result = {}
    queue.append((root,0))
    while queue:
        e,line = queue.popleft()
        if line not in result:
            result[line] = e.val
            if e.left:
                queue.append((e.left,line-1))
            if e.right:
                queue.append((e.right,line+1))
    for value in sorted(result.items()):
        ans.append(result[1])
    return ans

# TC O(NlogN) due to sorting
# SC O(N)