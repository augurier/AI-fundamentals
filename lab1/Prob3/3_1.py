import copy
import queue
import matplotlib.pyplot as plt
import matplotlib as mpl

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
    
def up(old_point, v):
    a = old_point.a
    b = old_point.b
    cnt = old_point.cnt + v
    new_point = points(a-1, b, 'u', cnt, old_point)
    return new_point
def down(old_point, v):
    a = old_point.a
    b = old_point.b
    cnt = old_point.cnt + v
    new_point = points(a+1, b, 'd', cnt, old_point)
    return new_point
def left(old_point, v):
    a = old_point.a
    b = old_point.b
    cnt = old_point.cnt + v
    new_point = points(a, b-1, 'l', cnt, old_point)
    return new_point
def right(old_point, v):
    a = old_point.a
    b = old_point.b
    cnt = old_point.cnt + v
    new_point = points(a, b+1, 'r', cnt, old_point)
    return new_point

def move(maze, n, m, old_point):
    ret = []
    a = old_point.a
    b = old_point.b
    direct = old_point.direct

    if a != 0 and direct != 'd' and maze[a-1][b] != 1:
        if maze[a][b] == 2 or maze[a][b] == 5:
            ret.append(up(old_point, 2))
        else:
            ret.append(up(old_point, 1))
    if b != 0 and direct != 'r' and maze[a][b-1] != 1:
        if maze[a][b] == 2 or maze[a][b] == 5:
            ret.append(left(old_point, 2))
        else:
            ret.append(left(old_point, 1))
    if a != n-1 and direct != 'u' and maze[a+1][b] != 1:
        if maze[a][b] == 2 or maze[a][b] == 5:
            ret.append(down(old_point, 2))
        else:
            ret.append(down(old_point, 1))   
    if b != m-1 and direct != 'l' and maze[a][b+1] != 1:
        if maze[a][b] == 2 or maze[a][b] == 5:
            ret.append(right(old_point, 2))
        else:
            ret.append(right(old_point, 1))           
    return ret
    

def dijkstra(maze, n, m):
    q = queue.PriorityQueue()
    point0 = points(0, 0, '', 0, None)
    q.put(point0)
    cover = set()
    cover.add((point0.a, point0.b))
    
    while(not q.empty()):
        old_point = q.get()
        if(finish(old_point, n, m)):
            return old_point
        
        new_points = move(maze, n, m, old_point)
        maze[old_point.a][old_point.b] += 3
        for new_point in new_points:
            if (new_point.a,new_point.b) not in cover:
                q.put(new_point)
                cover.add((new_point.a,new_point.b))
                
    print('no path exist!')
    return None

def dfs(maze, n, m):
    min = n*m
    ret = None
    q = []
    point0 = points(0, 0, '', 0, None)
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
        if maze[old_point.a][old_point.b] < 3:
            maze[old_point.a][old_point.b] += 3
        new_cover = copy.deepcopy(cover)
        for new_point in new_points:
            if (new_point.a,new_point.b) not in cover:
                new_cover.add((new_point.a,new_point.b))
                q.append((new_point, new_cover))                
    if(ret == None):            
        print('no path exist!')
    return ret

def bfs(maze, n, m):
    min = n*m
    ret = None
    q = queue.Queue()
    point0 = points(0, 0, '', 0, None)
    cover0 = set()
    cover0.add((point0.a, point0.b))    
    q.put((point0, cover0))

    
    while(not q.empty()):
        old_point, cover = q.get()    
        if(finish(old_point, n, m)):
            if old_point.cnt < min:
                min = old_point.cnt
                ret = old_point
            continue
        
        new_points = move(maze, n, m, old_point)
        if maze[old_point.a][old_point.b] < 3:
            maze[old_point.a][old_point.b] += 3
        new_cover = copy.deepcopy(cover)
        for new_point in new_points:
            if (new_point.a,new_point.b) not in cover:
                new_cover.add((new_point.a,new_point.b))
                q.put((new_point, new_cover))                
    if(ret == None):            
        print('no path exist!')
    return ret


def mahattan(n, m, a, b):
    return n-1-a + m-1-b

def astar(maze, n, m):
    q = queue.PriorityQueue()
    point0 = points2(0, 0, '', 0, None, mahattan(n, m, 0, 0))
    q.put(point0)
    cover = set()
    cover.add((point0.a, point0.b))
    
    while(not q.empty()):
        old_point = q.get()
        if(finish(old_point, n, m)):
            return old_point
        
        new_points = move(maze, n, m, old_point)
        maze[old_point.a][old_point.b] += 3
        for new_point0 in new_points:
            value = mahattan(n, m, new_point0.a, new_point0.b) + new_point0.cnt
            new_point = points2(new_point0.a, new_point0.b, new_point0.direct, new_point0.cnt, new_point0.father, value)
            if (new_point.a,new_point.b) not in cover:
                q.put(new_point)
                cover.add((new_point.a,new_point.b))
                
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
    colors = ['white', 'black', 'blue', 'yellow', 'green']
    bounds = [0,1,2,3,4,6]
    cmap = mpl.colors.ListedColormap(colors)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    plt.imshow(maze, cmap=cmap, norm=norm, interpolation='none')

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
    line = []
    for x in str0.split(' '):
        if x != '0' and x != '1':
            x = '2'
        line.append(int(x))
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

'''
5 5
0 0 0 0 0
1 2 1 1 0
0 0 0 0 0
0 1 1 1 1
0 0 0 0 0

5 5
0 0 0 0 0
1 1 1 1 5
0 0 0 0 0
10 10 0 0 0
0 10 0 0 0

5 5
0 0 0 0 0
0 1 0 1 0
2 0 0 0 0
0 1 0 1 0
0 0 0 0 0
'''
