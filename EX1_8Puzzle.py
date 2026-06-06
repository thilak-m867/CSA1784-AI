from queue import PriorityQueue

goal_state = (1,2,3,4,5,6,7,8,0)

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i*3+j]
            if tile != 0 :
                x, y = (tile-1)//3, (tile-1)%3
                distance += abs(x-i) + abs(y-j)
    return distance

def successors(state):
    result = []
    i = state.index(0)
    if i%3 != 0:
        s = list(state); s[i], s[i-1] = s[i-1], s[i]; result.append(tuple(s))
    if i%3 != 2:
        s = list(state); s[i], s[i+1] = s[i+1], s[i]; result.append(tuple(s))
    if i//3 != 0:
        s = list(state); s[i], s[i-3] = s[i-3], s[i]; result.append(tuple(s))
    if i//3 != 2:
        s = list(state); s[i], s[i+3] = s[i+3], s[i]; result.append(tuple(s))
    
    return result

def solve(initial):
    frontier = PriorityQueue()
    frontier.put((heuristic(initial), initial))
    explored = set()
    state = frontier.get()
    while not frontier.empty(): 
        #/////////////////////////////
        if state == goal_state: return True
        explored.add(state)
        for s in successors(state):
            if s not in explored:
                frontier.put(heuristic(s) + len(explored), s)
    return False

initial_state = (2,8,3,1,6,4,7,0,5)

if solve(initial_state):
    print("solvable")
else:
    print("The puzzle is unsolvable...")

