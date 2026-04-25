
def is_valid(grid, n, row, col, value):
    # Check if the value can be placed at grid[row][col]
    if row > 0 and grid[row-1][col] == value:  # check above
        return False
    if col > 0 and grid[row][col-1] == value:  # check left
        return False
    return True

def backtrack(grid, n, q, pos, counts):
    if pos == n * n:
        # Check conditions for zeros at specific positions
        if grid.count(0) >= 2:
            counts[0] += 1
        return

    row, col = divmod(pos, n)

    for value in range(q):
        if is_valid(grid, n, row, col, value):
            grid[row][col] = value
            backtrack(grid, n, q, pos + 1, counts)
            grid[row][col] = -1  # Reset the position

def count(n, q):
    counts = [0]  # List to hold count as mutable object
    grid = [[-1] * n for _ in range(n)]  # Initialize grid with -1 (unassigned)
    backtrack(grid, n, q, 0, counts)
    return counts[0]

# Example usage
result = count(2, 2)
print(result)  # Should output the number of valid configurations
