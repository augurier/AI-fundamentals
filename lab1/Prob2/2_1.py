import copy
import pickle
def finish(arr8):
    if(arr8 == [['1', '2', '3'], ['4', '5', '6'], ['7', '8', 'x']]):
        return True
    else:
        return False
    
def arr_to_tup(arr8):
    ret = []
    for i in range(3):
        for j in range(3):
            ret.append(arr8[i][j])
    return tuple(ret)

def up(arr8, a, b):
    Arr8 = pickle.loads(pickle.dumps(arr8))
    assert type(Arr8)== type(arr8)
    Arr8[a][b], Arr8[a-1][b] = Arr8[a-1][b], Arr8[a][b]
    return Arr8, a-1, b, 'up'
def down(arr8, a, b):
    Arr8 = pickle.loads(pickle.dumps(arr8))
    assert type(Arr8)== type(arr8)
    Arr8[a][b], Arr8[a+1][b] = Arr8[a+1][b], Arr8[a][b]
    return Arr8, a+1, b, 'down'
def left(arr8, a, b):
    Arr8 = pickle.loads(pickle.dumps(arr8))
    assert type(Arr8)== type(arr8)
    Arr8[a][b], Arr8[a][b-1] = Arr8[a][b-1], Arr8[a][b]
    return Arr8, a, b-1, 'left'
def right(arr8, a, b):
    Arr8 = pickle.loads(pickle.dumps(arr8))
    assert type(Arr8)== type(arr8)
    Arr8[a][b], Arr8[a][b+1] = Arr8[a][b+1], Arr8[a][b]
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
    cover.add(arr_to_tup(arr80))
    
    while(len(q) > 0):
        arr8_curr, a_curr, b_curr, direct = q.pop()
        if finish(arr8_curr):
            return 1
        states = move(arr8_curr, a_curr, b_curr, direct)
        for state in states:
            tup0 = arr_to_tup(state[0])
            if tup0 not in cover:
                q.append(state)
                cover.add(tup0)
    return 0

str0 = input().split(' ')
arr8 = []
for i in range(3):
    line = []
    for j in range(3):
        fig = str0[i*3 + j]
        line.append(fig)
        if fig == 'x':
            a = i
            b = j
    arr8.append(line)
#print(arr8)
print(dfs(arr8, a, b))
