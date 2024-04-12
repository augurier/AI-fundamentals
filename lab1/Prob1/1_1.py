import queue

def bfs(graph, n):
    if n == 1:
        return 0
    q = queue.Queue()
    q.put((1, 0))
    cover = set()
    while(not q.empty()):
        plot, dis = q.get()
        if(plot == n):
            return dis
        if(plot in cover):
            continue
        cover.add(plot)
        
        for neighbor in graph[plot].keys():
            q.put((neighbor, dis+1))
    return -1       

n, m = map(int,input().split(' '))
graph = {}
for i in range(1, m+1):
    graph.setdefault(i, {})
for i in range(m):
    x, y = map(int, input().split(' '))
    graph[x][y] = 1
        
print(bfs(graph, n))

