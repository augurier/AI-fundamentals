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

def up(arr8, a, b):
    Arr8 = swap(arr8, locate(a-1, b), locate(a, b))
    return Arr8, a-1, b, 'up'
def down(arr8, a, b):
    Arr8 = swap(arr8, locate(a+1, b), locate(a, b))
    return Arr8, a+1, b, 'down'
def left(arr8, a, b):
    Arr8 = swap(arr8, locate(a, b-1), locate(a, b))
    return Arr8, a, b-1, 'left'
def right(arr8, a, b):
    Arr8 = swap(arr8, locate(a, b+1), locate(a, b))
    return Arr8, a, b+1, 'right'

def move(arr8, a, b, direct):
    ret = []
    if a != 0 and direct != 'down':
        ret.append(up(arr8, a, b))
    if a != 2 and direct != 'up':
        ret.append(down(arr8, a, b))
    if b != 0 and direct != 'right':
        ret.append(left(arr8, a, b))
    if b != 2 and direct != 'left':
        ret.append(right(arr8, a, b))
    return ret

def dfs(arr80, a0, b0):
    q = []
    q.append((arr80, a0, b0, 'up'))
    cover = set()
    cover.add(arr80)
    
    while(len(q) > 0):
        arr8_curr, a_curr, b_curr, direct = q.pop()
        if finish(arr8_curr):
            return 1
        states = move(arr8_curr, a_curr, b_curr, direct)
        for state in states:
            if state[0] not in cover:
                q.append(state)
                cover.add(state[0])
    return 0

arr8 = input().replace(' ','')
pos = arr8.find('x')
a = pos // 3
b = pos % 3
#print(arr8)
print(dfs(arr8, a, b))
