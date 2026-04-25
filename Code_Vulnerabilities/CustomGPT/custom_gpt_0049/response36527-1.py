
def is_valid(grid, row, col, n, value):
    # Check the left neighbor
    if col > 0 and grid[row][col - 1] == value:
        return False
    # Check the right neighbor
    if col < n - 1 and grid[row][col + 1] == value:
        return False
    # Check the top neighbor
    if row > 0 and grid[row - 1][col] == value:
        return False
    # Check the bottom neighbor
    if row < n - 1 and grid[row + 1][col] == value:
        return False
    return True

def backtrack(grid, pos, n, q, count):
    if pos == n * n:
        count[0] += 1
        return

    row, col = divmod(pos, n)
    for value in range(q):
        if (row, col) in zero_positions:
            if value == 0:
                grid[row][col] = value
                backtrack(grid, pos + 1, n, q, count)
                grid[row][col] = -1  # Reset
        else:
            if is_valid(grid, row, col, n, value):
                grid[row][col] = value
                backtrack(grid, pos + 1, n, q, count)
                grid[row][col] = -1  # Reset

def count_assignments(n, q, zero_positions):
    global count
    count = [0]
    grid = [[-1] * n for _ in range(n)]
    backtrack(grid, 0, n, q, count)
    return count[0]

# Update the positions (i,j) and (k,l) you want to be zero
zero_positions = {(0, 0), (1, 1)}
result = count_assignments(2, 2, zero_positions)
print("Total valid assignments:", result)
