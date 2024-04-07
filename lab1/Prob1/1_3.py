import queue
INF = float('inf')

def dijkstra2(graph, n):
    if n == 1:
        return 0
    dis = [0]
    q = queue.PriorityQueue()
    for i in range(1, n+1):
        if(i in graph[1].keys()):
            dis.append(graph[1][i])
            q.put((graph[1][i], i))
        else:
            dis.append(INF)
    cover = set()
    cover.add(1)
    
    while(len(cover) < n):
        if q.empty():
            return -1
        a, plot = q.get()
        if plot in cover:
            continue
        if plot == n:
            return dis[n]
        
        cover.add(plot)
        for neighbor in graph[plot].keys():
            if(neighbor in cover):
                continue
            if(dis[plot] + graph[plot][neighbor] < dis[neighbor]):
                dis[neighbor] = dis[plot] + graph[plot][neighbor]
                q.put((dis[neighbor], neighbor))



n, m = map(int,input().split(' '))
graph = {}
for i in range(1, m+1):
    graph.setdefault(i, {})
for i in range(m):
    x, y, z = map(int, input().split(' '))
    graph[x][y] = z
    
print(dijkstra2(graph, n))