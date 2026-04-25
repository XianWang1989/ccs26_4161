
def is_valid(grid, row, col, value):
    # Check horizontal and vertical neighbors
    for i in range(-1, 2):
        if 0 <= row + i < len(grid):
            if 0 <= col < len(grid) and grid[row + i][col] == value:
                return False
    for j in range(-1, 2):
        if 0 <= col + j < len(grid):
            if 0 <= row < len(grid) and grid[row][col + j] == value:
                return False
    return True

def backtrack(grid, n, q, pos, results, pos1, pos2):
    if pos == n * n:
        if grid[pos1 // n][pos1 % n] == 0 and grid[pos2 // n][pos2 % n] == 0:
            results[0] += 1
        return

    row, col = divmod(pos, n)

    for value in range(q):
        if is_valid(grid, row, col, value):
            grid[row][col] = value
            backtrack(grid, n, q, pos + 1, results, pos1, pos2)
            grid[row][col] = -1  # Reset for backtracking

def count(n, q):
    results = [0]
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 != pos2:  # Ensure positions are distinct
                grid = [[-1] * n for _ in range(n)]  # Initialize grid with -1
                grid[pos1 // n][pos1 % n] = 0
                grid[pos2 // n][pos2 % n] = 0
                backtrack(grid, n, q, 0, results, pos1, pos2)
    return results

# Test the function
print(count(2, 2))
