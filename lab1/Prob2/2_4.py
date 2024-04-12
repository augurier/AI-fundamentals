import queue
import time

class status:
    def __init__(self, arr8, a, b, direct, cnt, value, father):
        self.arr8 = arr8
        self.a = a
        self.b = b
        self.direct = direct
        self.cnt = cnt
        self.value = value
        self.father = father
    def __lt__(self, other):
        return self.value < other.value

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

def wrong_pos(arr8):
    cnt = 0
    pos = 1
    for i in range(9):
        if str(pos) != arr8[i]:
            cnt += 1
        pos += 1
    return cnt-1

def up(old_state):
    arr8 = old_state.arr8
    a = old_state.a
    b = old_state.b
    cnt = old_state.cnt + 1
    Arr8 = swap(arr8, locate(a-1, b), locate(a, b))
    new_state = status(Arr8, a-1, b, 'u', cnt, wrong_pos(Arr8) + cnt, old_state)
    return new_state
def down(old_state):
    arr8 = old_state.arr8
    a = old_state.a
    b = old_state.b
    cnt = old_state.cnt + 1
    Arr8 = swap(arr8, locate(a+1, b), locate(a, b))
    new_state = status(Arr8, a+1, b, 'd', cnt, wrong_pos(Arr8) + cnt, old_state)
    return new_state
def left(old_state):
    arr8 = old_state.arr8
    a = old_state.a
    b = old_state.b
    cnt = old_state.cnt + 1
    Arr8 = swap(arr8, locate(a, b-1), locate(a, b))
    new_state = status(Arr8, a, b-1, 'l', cnt, wrong_pos(Arr8) + cnt, old_state)
    return new_state
def right(old_state):
    arr8 = old_state.arr8
    a = old_state.a
    b = old_state.b
    cnt = old_state.cnt + 1
    Arr8 = swap(arr8, locate(a, b+1), locate(a, b))
    new_state = status(Arr8, a, b+1, 'r', cnt, wrong_pos(Arr8) + cnt, old_state)
    return new_state

def move(old_state):
    ret = []
    a = old_state.a
    b = old_state.b
    direct = old_state.direct
    if a != 0 and direct != 'd':
        ret.append(up(old_state))
    if a != 2 and direct != 'u':
        ret.append(down(old_state))
    if b != 0 and direct != 'r':
        ret.append(left(old_state))
    if b != 2 and direct != 'l':
        ret.append(right(old_state))
    return ret




def astar(arr80, a0, b0):
    q = queue.PriorityQueue()
    value0 = wrong_pos(arr80)
    state0 = status(arr80, a0, b0, '', 0, value0, None)
    q.put(state0)
    cover = set()
    cover.add(arr80)
    
    while(not q.empty()):
        old_state = q.get()
        if finish(old_state.arr8):
            return old_state
        states = move(old_state)
        for state in states:
            if state.arr8 not in cover:
                q.put(state)
                cover.add(state.arr8)
    return None

def print_ans(ans, arr80):
    if ans.arr8 == arr80:
        return
    else:
        print_ans(ans.father, arr80)
        print(ans.direct, end='')
        
def solvable(str0):
    cnt = 0
    for i in range(9):
        if str0[i] == 'x':
            continue
        for j in range(i):
            if str0[j] == 'x':
                continue
            if str0[i] < str0[j]:
                cnt += 1
    
    if cnt % 2 == 0:
        return True
    else:
        return False
        

arr80 = input().replace(' ','')
pos = arr80.find('x')
a = pos // 3
b = pos % 3
#print(arr8)
if not solvable(arr80):
    print('unsolvable')
else:
    # t = time.time()
    ans = astar(arr80, a, b)
    print_ans(ans, arr80)
    # e = time.time()
    # print(e-t)
