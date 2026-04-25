
def is_valid(grid, n, r, c, value):
    # Check neighbors (top, bottom, left, right)
    if r > 0 and grid[r-1][c] == value:
        return False
    if r < n-1 and grid[r+1][c] == value:
        return False
    if c > 0 and grid[r][c-1] == value:
        return False
    if c < n-1 and grid[r][c+1] == value:
        return False
    return True

def backtrack(grid, n, q, idx, pos1, pos2):
    if idx == n * n:
        return 1  # Found a valid configuration

    r, c = divmod(idx, n)
    total = 0
    for value in range(q):
        if (idx == pos1 or idx == pos2) and value != 0:
            continue  # Ensure the specified positions are 0
        if is_valid(grid, n, r, c, value):
            grid[r][c] = value
            total += backtrack(grid, n, q, idx + 1, pos1, pos2)
            grid[r][c] = -1  # Reset the grid position

    return total

def count(n, q):
    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            grid = [[-1] * n for _ in range(n)]  # Initialize grid with -1
            total = backtrack(grid, n, q, 0, pos1, pos2)
            result.append(total)
    return result

# Example usage:
print(count(2, 2))  # Output should match the expected results
