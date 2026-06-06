from collections import deque

# Step 1 & 2: Define initial and goal states
# State format: (missionaries_left, cannibals_left, boat_position)
# boat_position: 1 for left bank, 0 for right bank
INITIAL_STATE = (3, 3, 1)
GOAL_STATE = (0, 0, 0)

# Step 3: Validate each state
def is_valid(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left
    
    # Check if numbers are out of bounds
    if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False
        
    # Cannibals must never outnumber missionaries on the left side
    if m_left > 0 and c_left > m_left:
        return False
        
    # Cannibals must never outnumber missionaries on the right side
    if m_right > 0 and c_right > m_right:
        return False
        
    return True

# Step 4: Generate successors by moving 1 or 2 people across the river
def get_successors(state):
    successors = []
    m_left, c_left, boat = state
    
    # Possible boat combinations: (missionaries_to_move, cannibals_to_move)
    # The boat can carry 1 or 2 people
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    for m_move, c_move in moves:
        if boat == 1:  # Moving from Left to Right
            next_state = (m_left - m_move, c_left - c_move, 0)
        else:          # Moving from Right to Left
            next_state = (m_left + m_move, c_left + c_move, 1)
            
        if is_valid(next_state):
            successors.append(next_state)
            
    return successors

# Step 5: Use BFS to find the shortest path from initial to goal state
def solve_bfs():
    # Queue stores tuples of (current_state, path_taken_to_reach_it)
    queue = deque([(INITIAL_STATE, [INITIAL_STATE])])
    visited = set([INITIAL_STATE])
    
    while queue:
        current_state, path = queue.popleft()
        
        # Check if goal is reached
        if current_state == GOAL_STATE:
            return path  # Step 6: Return the path of states
            
        for successor in get_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [successor]))
                
    return None

def print_solution(path):
    if not path:
        print("No solution found.")
        return
        
    print(f"Solution found in {len(path) - 1} moves:\n")
    print(f"{'Left Bank':<15} | {'Boat':<6} | {'Right Bank':<15}")
    print("-" * 44)
    
    for state in path:
        m_l, c_l, boat = state
        m_r, c_r = 3 - m_l, 3 - c_l
        
        b_pos = "Left" if boat == 1 else "Right"
        left_str = f"{m_l}M, {c_l}C"
        right_str = f"{m_r}M, {c_r}C"
        
        print(f"{left_str:<15} | {b_pos:<6} | {right_str:<15}")

# Execute the program
solution_path = solve_bfs()
print_solution(solution_path)