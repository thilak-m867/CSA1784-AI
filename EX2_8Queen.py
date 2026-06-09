def solve_queen(n):
    board = [-1] * n
    result = []
    def is_valid(row, col):
        for i in range(row):
            if board[i] == col or abs(row - i) == abs(col - board[i]):
                return False
        return True
    def backtrack(row):
        if row == n:
            result.append(list (board)); return
        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    backtrack(0)
    return result

solutions = solve_queen(8)

print(f"Total solutions: {len(solutions)}")
for solution in solutions[:1]:
    for row in range(8):
        line = ' '
        for col in range(8):
            line += 'Q' if solution[row] == col else '- '
        print (line)

