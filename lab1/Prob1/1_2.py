INF = float('inf')

def shortest(dis, cover, n):
    min = INF
    cnt = -1
    for i in range(1, n+1):
        if(i not in cover):
            if(dis[i] < min):
                min = dis[i]
                cnt = i
    return cnt

def dijkstra1(graph, n):
    if n == 1:
        return 0
    dis = [0]
    for i in range(1, n+1):
        if(i in graph[1].keys()):
            dis.append(graph[1][i])
        else:
            dis.append(INF)
    cover = set()
    cover.add(1)
    
    while(len(cover) < n):
        plot = shortest(dis, cover, n)
        if plot == -1:
            return -1
        if plot == n:
            return dis[n]
        
        cover.add(plot)
        for neighbor in graph[plot].keys():
            if(neighbor in cover):
                continue
            if(dis[plot] + graph[plot][neighbor] < dis[neighbor]):
                dis[neighbor] = dis[plot] + graph[plot][neighbor]



n, m = map(int,input().split(' '))
graph = {}
for i in range(1, m+1):
    graph.setdefault(i, {})
for i in range(m):
    x, y, z = map(int, input().split(' '))
    graph[x][y] = z
    
print(dijkstra1(graph, n))