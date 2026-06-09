# Step 1: Represent state variables
# Position: (row, col) tuple
# Grid: 2D tuple (tuples are immutable and hashable, making them perfect for a 'visited' set)

INITIAL_GRID = (
    (1, 0, 1),
    (0, 1, 0),
    (1, 0, 1)
)
INITIAL_POSITION = (0, 0)

# Helper function to check if all cells in a grid are clean
def is_goal_state(grid):
    return all(cell == 0 for row in grid for cell in row)

# Step 2: Generate successor states by moving in 4 directions and cleaning dirty cells
def get_successors(position, grid):
    successors = []
    r, c = position
    max_r, max_c = len(grid), len(grid[0])
    
    # Action A: Clean the current cell if it's dirty
    if grid[r][c] == 1:
        # Create a new grid representation with the current cell set to 0 (clean)
        new_grid = list(list(row) for row in grid)
        new_grid[r][c] = 0
        immutable_grid = tuple(tuple(row) for row in new_grid)
        successors.append(((r, c), immutable_grid, "CLEAN"))
    
    # Action B: Move in 4 directions (Up, Down, Left, Right)
    directions = [(-1, 0, "MOVE_UP"), (1, 0, "MOVE_DOWN"), (0, -1, "MOVE_LEFT"), (0, 1, "MOVE_RIGHT")]
    for dr, dc, action_name in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < max_r and 0 <= nc < max_c:
            successors.append(((nr, nc), grid, action_name))
            
    return successors

# Step 3 & 4: Use DFS to explore states and track visited entries to avoid loops
def solve_vacuum_dfs(initial_pos, initial_grid):
    # Stack stores: (current_position, current_grid, execution_path)
    # Using a list as a LIFO stack for Depth-First Search
    stack = [(initial_pos, initial_grid, [(initial_pos, "START")])]
    visited = set()
    
    while stack:
        position, grid, path = stack.pop()
        
        # Goal check: Return True if the room is fully cleaned (Step 5)
        if is_goal_state(grid):
            print_execution_log(path, grid)
            return True
            
        # Create a unique state signature for tracking
        state_signature = (position, grid)
        
        if state_signature not in visited:
            visited.add(state_signature)
            
            # Retrieve adjacent actions and add them to the stack
            for next_pos, next_grid, action in get_successors(position, grid):
                if (next_pos, next_grid) not in visited:
                    new_path = path + [(next_pos, action)]
                    stack.append((next_pos, next_grid, new_path))
                    
    return False

def print_execution_log(path, final_grid):
    print("Goal State Reached! Execution Path:")
    print("-" * 40)
    for index, (pos, action) in enumerate(path):
        print(f"Step {index}: Action = {action:<10} | Robot Position = {pos}")
    print("-" * 40)
    print("Final Environment Grid (All Clean):")
    for row in final_grid:
        print(row)

# Execute the simulation
print("Starting Vacuum Cleaner Simulation...")
is_cleanable = solve_vacuum_dfs(INITIAL_POSITION, INITIAL_GRID)
print(f"\nResult: Return {is_cleanable}")
