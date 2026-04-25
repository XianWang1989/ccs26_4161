
def is_valid(grid, r, c, value, n):
    # Check horizontally and vertically adjacent cells
    if r > 0 and grid[r - 1][c] == value:  # Check top
        return False
    if r < n - 1 and grid[r + 1][c] == value:  # Check bottom
        return False
    if c > 0 and grid[r][c - 1] == value:  # Check left
        return False
    if c < n - 1 and grid[r][c + 1] == value:  # Check right
        return False
    return True

def backtrack(grid, n, q, pos1, pos2, result, idx=0):
    if idx == n * n:
        if grid[pos1 // n][pos1 % n] == 0 and grid[pos2 // n][pos2 % n] == 0:
            result[0] += 1
        return

    r = idx // n
    c = idx % n
    for value in range(q):
        if is_valid(grid, r, c, value, n):
            grid[r][c] = value
            backtrack(grid, n, q, pos1, pos2, result, idx + 1)
            grid[r][c] = -1  # Reset for the backtrack

def count(n, q):
    result = [0]  # Use a list to capture the count in a mutable way
    grid = [[-1] * n for _ in range(n)]  # Initialize the grid with -1
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 != pos2:  # Make sure positions are not the same
                grid = [[-1] * n for _ in range(n)]  # Reset grid for each configuration
                backtrack(grid, n, q, pos1, pos2, result)
    return result[0]

# Example usage
print(count(2, 2))  # Example output
