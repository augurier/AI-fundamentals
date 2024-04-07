import queue

def bfs(graph, n):
    if n == 1:
        return 0
    q = queue.Queue()
    q.put(1)
    cover = set()
    cover.add(1)
    dis = 1
    while(not q.empty()):
        plot = q.get()
        for neighbor in graph[plot].keys():
            if(neighbor == n):
                return dis
            
            if(neighbor not in cover):
                q.put(neighbor)
                cover.add(neighbor)
        dis += 1
    return -1        

n, m = map(int,input().split(' '))
graph = {}
for i in range(1, m+1):
    graph.setdefault(i, {})
for i in range(m):
    x, y = map(int, input().split(' '))
    graph[x][y] = 1
        
print(bfs(graph, n))

