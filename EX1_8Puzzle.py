import heapq

# Define the goal state configuration
# 0 represents the empty blank space
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def get_manhattan_distance(state):
    """Calculates the sum of Manhattan distances of tiles from their goal positions."""
    distance = 0
    for current_idx, tile in enumerate(state):
        if tile != 0:
            # Current coordinates on a 3x3 grid
            current_row, current_col = current_idx // 3, current_idx % 3
            
            # Target coordinates in the goal state (tile 1 is at index 0, tile 2 at index 1...)
            target_idx = tile - 1
            target_row, target_col = target_idx // 3, target_idx % 3
            
            distance += abs(current_row - target_row) + abs(current_col - target_col)
    return distance

def get_successors(state):
    """Generates all valid next states by moving the blank tile (0) Up, Down, Left, or Right."""
    successors = []
    blank_idx = state.index(0)
    row, col = blank_idx // 3, blank_idx % 3
    
    # Define directional movements: (row_change, col_change)
    moves = {
        "UP": (-1, 0),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
        "RIGHT": (0, 1)
    }
    
    for move_name, (dr, dc) in moves.items():
        new_row, new_col = row + dr, col + dc
        
        # Check if the move stays within the boundaries of the 3x3 grid
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_idx = new_row * 3 + new_col
            
            # Swap the blank space with the target tile
            state_list = list(state)
            state_list[blank_idx], state_list[new_blank_idx] = state_list[new_blank_idx], state_list[blank_idx]
            
            successors.append(tuple(state_list))
            
    return successors

def solve_8_puzzle(initial_state):
    """Solves the 8-puzzle using A* Search and prints the step-by-step path."""
    # The open list priority queue stores elements as: (f_score, g_score, current_state)
    # g_score represents the exact path cost (number of moves from start)
    open_list = []
    initial_h = get_manhattan_distance(initial_state)
    heapq.heappush(open_list, (initial_h, 0, initial_state))
    
    # Track parent pointers to reconstruct the solution path later
    came_from = {initial_state: None}
    # Track the minimum g_score (moves) required to reach each state
    g_score = {initial_state: 0}
    
    while open_list:
        # Select the state with the lowest f_score (f = g + h)
        current_f, current_g, current_state = heapq.heappop(open_list)
        
        # Goal Check
        if current_state == GOAL_STATE:
            return reconstruct_path(came_from, current_state)
            
        for successor in get_successors(current_state):
            tentative_g = current_g + 1
            
            # If we found a shorter path to this state or it hasn't been visited
            if successor not in g_score or tentative_g < g_score[successor]:
                came_from[successor] = current_state
                g_score[successor] = tentative_g
                f_score = tentative_g + get_manhattan_distance(successor)
                heapq.heappush(open_list, (f_score, tentative_g, successor))
                
    return None # Return None if the puzzle is unsolvable

def reconstruct_path(came_from, current_state):
    """Traces back through the parent map to assemble the path from start to goal."""
    path = []
    while current_state is not None:
        path.append(current_state)
        current_state = came_from[current_state]
    return path[::-1] # Reverse the path to get chronological order

def print_board(state):
    """Helper function to print a neat 3x3 layout representation of a state."""
    for i in range(0, 9, 3):
        row = [str(x) if x != 0 else " " for x in state[i:i+3]]
        print(" | ".join(row))
    print("-" * 9)

# --- Execute Code ---

# Configuration representation (flattened 3x3 grid layout)
# 2 8 3
# 1 6 4
# 7 . 5
start_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)

print("Starting A* Search on Initial Board Layout:\n")
print_board(start_state)

solution_path = solve_8_puzzle(start_state)

if solution_path:
    print(f"Goal State Reached successfully in {len(solution_path) - 1} moves!\n")
    for step_num, state in enumerate(solution_path):
        print(f"Step {step_num}:")
        print_board(state)
else:
    print("This puzzle configuration is mathematically unsolvable.")
