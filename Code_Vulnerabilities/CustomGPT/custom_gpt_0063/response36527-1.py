
def is_valid(grid, r, c, value, n):
    """Check if placing value at grid[r][c] is valid."""
    # Check left
    if c > 0 and grid[r][c-1] == value:
        return False
    # Check right
    if c < n - 1 and grid[r][c+1] == value:
        return False
    # Check top
    if r > 0 and grid[r-1][c] == value:
        return False
    # Check bottom
    if r < n - 1 and grid[r+1][c] == value:
        return False
    return True

def dp(grid, pos, n, q, pos1, pos2, memo):
    """Recursive function to compute the number of valid assignments."""
    if pos == n * n:
        return 1 if grid[pos1] == 0 and grid[pos2] == 0 else 0

    if (tuple(grid), pos) in memo:
        return memo[(tuple(grid), pos)]

    count = 0
    for value in range(q):
        r, c = divmod(pos, n)
        if is_valid(grid, r, c, value, n):
            grid[pos] = value
            count += dp(grid, pos + 1, n, q, pos1, pos2, memo)
            grid[pos] = -1  # Reset the position

    memo[(tuple(grid), pos)] = count
    return count

def count(n, q):
    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            grid = [-1] * (n * n)  # Initialize grid with -1 (unassigned)
            memo = {}
            total = dp(grid, 0, n, q, pos1, pos2, memo)
            result.append(total)
    return result

# Example usage
print(count(2, 2))  # Output should match the expected result
