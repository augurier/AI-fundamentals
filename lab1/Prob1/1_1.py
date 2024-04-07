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
        if(plot not in graph.keys()):
            continue
        neighbor = graph[plot]
        for i in neighbor:
            if(i == n):
                return dis
            
            if(i not in cover):
                q.put(i)
                cover.add(i)
        dis += 1
    return -1        

n, m = map(int,input().split(' '))
graph = {}
for i in range(1, m+1):
    graph.setdefault(i, [])
for i in range(m):
    x, y = map(int, input().split(' '))
    graph[x].append(y)
        
print(bfs(graph, n))
