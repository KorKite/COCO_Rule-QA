import sys
n, m = map(int, sys.stdin.readline().split(" "))
graph = [[False for i in range(n)] for i in range(n)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split(" "))
    graph[a-1][b-1] = True
    graph[b-1][a-1] = True

visited = [False for i in range(n)]
def dfs_search(size, visited, start_node):
    visited[start_node] = True
    nodes = graph[start_node]
    for i in range(size):
        if nodes[i] == True and visited[i] == False:
            search(size, visited, i)
            
def bfs_search(size, visited, start_node):
    visited[start_node] = True
    queue = []
    queue.append(start_node)
    while len(queue) != 0:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = True
        nodes = graph[v]
        for i in range(size):
            if nodes[i] == True and not visited[i]:
                queue.append(i)
    return

count = 0

for i in range(n):
    if not visited[i]:
        dfs_search(n, visited, i)
        count += 1
print(count)
