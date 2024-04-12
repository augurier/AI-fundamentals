import queue
import time
def swap(str0, x, y):
    if x > y:
        x, y = y, x
    return str0[:x:] + str0[y] + str0[x+1:y:] + str0[x] + str0[y+1::]

def locate(a, b):
    return a*3 + b

def finish(arr8):
    if(arr8 == '12345678x'):
        return True
    else:
        return False

def up(arr8, a, b, cnt):
    Arr8 = swap(arr8, locate(a-1, b), locate(a, b))
    return Arr8, a-1, b, 'up', cnt
def down(arr8, a, b, cnt):
    Arr8 = swap(arr8, locate(a+1, b), locate(a, b))
    return Arr8, a+1, b, 'down', cnt
def left(arr8, a, b, cnt):
    Arr8 = swap(arr8, locate(a, b-1), locate(a, b))
    return Arr8, a, b-1, 'left', cnt
def right(arr8, a, b, cnt):
    Arr8 = swap(arr8, locate(a, b+1), locate(a, b))
    return Arr8, a, b+1, 'right', cnt

def move(arr8, a, b, direct, cnt):
    ret = []
    cnt += 1
    if a != 0 and direct != 'down':
        ret.append(up(arr8, a, b, cnt))
    if a != 2 and direct != 'up':
        ret.append(down(arr8, a, b, cnt))
    if b != 0 and direct != 'right':
        ret.append(left(arr8, a, b, cnt))
    if b != 2 and direct != 'left':
        ret.append(right(arr8, a, b, cnt))
    return ret

def bfs(arr80, a0, b0):
    q = queue.Queue()
    q.put((arr80, a0, b0, '', 0))
    cover = set()
    cover.add(arr80)
    
    while(not q.empty()):
        arr8_curr, a_curr, b_curr, direct, cnt = q.get()
        if finish(arr8_curr):
            return cnt
        states = move(arr8_curr, a_curr, b_curr, direct, cnt)
        for state in states:
            if state[0] not in cover:
                q.put(state)
                cover.add(state[0])
    return -1

arr8 = input().replace(' ','')
pos = arr8.find('x')
a = pos // 3
b = pos % 3
#print(arr8)
#t = time.time()
print(bfs(arr8, a, b))
#e = time.time()
#print(e-t)
#6 4 7 8 5 x 3 2 1
