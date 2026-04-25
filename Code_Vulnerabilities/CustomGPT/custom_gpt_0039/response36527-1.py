
def is_valid(current_grid, row, col, value):
    # Check left, right, up, and down neighbors
    if col > 0 and current_grid[row][col - 1] == value:
        return False
    if col < len(current_grid) - 1 and current_grid[row][col + 1] == value:
        return False
    if row > 0 and current_grid[row - 1][col] == value:
        return False
    if row < len(current_grid) - 1 and current_grid[row + 1][col] == value:
        return False
    return True

def backtrack(n, q, current_grid, pos, results, pos1, pos2):
    if pos == n * n:
        # Count valid configuration with specified (0,0) positions
        if current_grid[pos1 // n][pos1 % n] == 0 and current_grid[pos2 // n][pos2 % n] == 0:
            results[tuple(map(tuple, current_grid))] = results.get(tuple(map(tuple, current_grid)), 0) + 1
        return

    row, col = divmod(pos, n)
    for value in range(q):
        if (row, col) in (pos1, pos2) and value != 0:
            continue  # Position must be 0
        if is_valid(current_grid, row, col, value):
            current_grid[row][col] = value  # Set value
            backtrack(n, q, current_grid, pos + 1, results, pos1, pos2)
            current_grid[row][col] = -1  # Reset for backtracking

def count(n, q):
    results = {}
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:
                continue  # Same position for both zeroes
            current_grid = [[-1] * n for _ in range(n)]  # -1 represents unassigned
            backtrack(n, q, current_grid, 0, results, (pos1 // n, pos1 % n), (pos2 // n, pos2 % n))

    return [results.get(k, 0) for k in sorted(results.keys())]

# Example usage
print(count(2, 2))
