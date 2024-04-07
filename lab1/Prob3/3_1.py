import copy
import queue
import matplotlib.pyplot as plt

class points:
    def __init__(self, a, b, direct, cnt, father):
        self.a = a
        self.b = b
        self.direct = direct
        self.cnt = cnt
        self.father = father
    def __lt__(self, other):
        return self.cnt < other.cnt
    
class points2(points):
    def __init__(self, a, b, direct, cnt, father, value):
        super().__init__(a, b, direct, cnt, father)
        self.value = value
    def __lt__(self, other):
        return self.value < other.value
    
def finish(point, n, m):
    if(point.a == n-1 and point.b == m-1):
        return True
    else:
        return False
    
def up(old_point):
    a = old_point.a
    b = old_point.b
    cnt = old_point.cnt + 1
    new_point = points(a-1, b, 'u', cnt, old_point)
    return new_point
def down(old_point):
    a = old_point.a
    b = old_point.b
    cnt = old_point.cnt + 1
    new_point = points(a+1, b, 'd', cnt, old_point)
    return new_point
def left(old_point):
    a = old_point.a
    b = old_point.b
    cnt = old_point.cnt + 1
    new_point = points(a, b-1, 'l', cnt, old_point)
    return new_point
def right(old_point):
    a = old_point.a
    b = old_point.b
    cnt = old_point.cnt + 1
    new_point = points(a, b+1, 'r', cnt, old_point)
    return new_point

def move(maze, n, m, old_point):
    ret = []
    a = old_point.a
    b = old_point.b
    direct = old_point.direct

    if a != 0 and direct != 'd' and maze[a-1][b] != 1:
        ret.append(up(old_point))
    if b != 0 and direct != 'r' and maze[a][b-1] != 1:
        ret.append(left(old_point))
    if a != n-1 and direct != 'u' and maze[a+1][b] != 1:
        ret.append(down(old_point))    
    if b != m-1 and direct != 'l' and maze[a][b+1] != 1:
        ret.append(right(old_point))            
    return ret
    

def dijkstra(maze, n, m):
    q = queue.PriorityQueue()
    point0 = points(0, 0, 'd', 0, None)
    q.put(point0)
    cover = set()
    cover.add((point0.a, point0.b))
    
    while(not q.empty()):
        old_point = q.get()
        if(finish(old_point, n, m)):
            return old_point
        
        new_points = move(maze, n, m, old_point)
        for new_point in new_points:
            if (new_point.a,new_point.b) not in cover:
                q.put(new_point)
                cover.add((new_point.a,new_point.b))
                maze[new_point.a][new_point.b] = 0.5
                
    print('no path exist!')
    return None

def dfs(maze, n, m):
    min = n*m
    ret = None
    q = []
    point0 = points(0, 0, 'd', 0, None)
    cover0 = set()
    cover0.add((point0.a, point0.b))    
    q.append((point0, cover0))

    
    while(len(q) > 0):
        old_point, cover = q.pop()
        if(finish(old_point, n, m)):
            if old_point.cnt < min:
                min = old_point.cnt
                ret = old_point
            continue
        
        new_points = move(maze, n, m, old_point)
        new_cover = copy.deepcopy(cover)
        for new_point in new_points:
            if (new_point.a,new_point.b) not in cover:
                new_cover.add((new_point.a,new_point.b))
                q.append((new_point, new_cover))                
                maze[new_point.a][new_point.b] = 0.5
    if(ret == None):            
        print('no path exist!')
    return ret

def bfs(maze, n, m):
    q = []
    point0 = points(0, 0, 'd', 0, None)
    q.append(point0)
    cover = set()
    cover.add((point0.a, point0.b))
    
    while(len(q) > 0):
        old_point = q.pop(0)
        if(finish(old_point, n, m)):
            return old_point
        
        new_points = move(maze, n, m, old_point)
        for new_point in new_points:
            if (new_point.a,new_point.b) not in cover:
                q.append(new_point)
                cover.add((new_point.a,new_point.b))
                maze[new_point.a][new_point.b] = 0.5
                
    print('no path exist!')
    return None

def mahattan(n, m, a, b):
    return n-1-a + m-1-b

def astar(maze, n, m):
    q = queue.PriorityQueue()
    point0 = points2(0, 0, 'd', 0, None, mahattan(n, m, 0, 0))
    q.put(point0)
    cover = set()
    cover.add((point0.a, point0.b))
    
    while(not q.empty()):
        old_point = q.get()
        if(finish(old_point, n, m)):
            return old_point
        
        new_points = move(maze, n, m, old_point)
        for new_point0 in new_points:
            value = mahattan(n, m, new_point0.a, new_point0.b) + new_point0.cnt
            new_point = points2(new_point0.a, new_point0.b, new_point0.direct, new_point0.cnt, new_point0.father, value)
            if (new_point.a,new_point.b) not in cover:
                q.put(new_point)
                cover.add((new_point.a,new_point.b))
                maze[new_point.a][new_point.b] = 0.5
                
    print('no path exist!')
    return None

       
def traceback_path(point):
    if point.a == 0 and point.b == 0:
        return [(point.a, point .b)]
    
    path = traceback_path(point.father)
    path.append((point.a, point.b))
    return path

def visualize_maze_with_path(maze, path, algorithm, pos):
    plt.subplot(2, 2, pos)
    #plt.figure(figsize=(len(maze[0]), len(maze)))
    plt.imshow(maze, cmap='Greys', interpolation='nearest')

    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, marker='o', markersize=8, color='red', linewidth=3)

    plt.xticks(range(len(maze[0])))
    plt.yticks(range(len(maze)))
    plt.gca().set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
    plt.gca().set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
    plt.grid(which="minor", color="black", linestyle='-', linewidth=2)
    plt.title(algorithm)

    plt.axis('on')
    #plt.show()
        

n, m = map(int, input().split(' '))
maze = []
for i in range(n):
    str0 = input()
    line = [int(x) for x in str0.split(' ')]
    maze.append(line)
#print(maze)

maze1 = copy.deepcopy(maze)
ans_point1 = bfs(maze1, n, m)
if ans_point1 == None:
    quit()
path1 = traceback_path(ans_point1)
visualize_maze_with_path(maze1, path1, "bfs", 1)
print(ans_point1.cnt)

maze2 = copy.deepcopy(maze)
ans_point2 = dfs(maze2, n, m)
path2 = traceback_path(ans_point2)
visualize_maze_with_path(maze2, path2, "dfs", 2)

maze3 = copy.deepcopy(maze)
ans_point3 = dijkstra(maze3, n, m)
path3 = traceback_path(ans_point3)
visualize_maze_with_path(maze3, path3, "dijkstra", 3)

maze4 = copy.deepcopy(maze)
ans_point4 = astar(maze4, n, m)
path4 = traceback_path(ans_point4)
visualize_maze_with_path(maze4, path4, "astar", 4)

plt.show()