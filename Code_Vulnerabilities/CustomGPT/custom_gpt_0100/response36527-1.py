
def is_valid(grid, n, row, col, value):
    # Check horizontal and vertical neighbors
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + d[0], col + d[1]
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == value:
            return False
    return True

def assign_values(n, q, grid, pos, results):
    if pos == n * n:  # If we've filled all positions
        results.append([grid[i][j] for i in range(n) for j in range(n)])
        return

    row, col = divmod(pos, n)
    for value in range(q):
        if is_valid(grid, n, row, col, value):
            grid[row][col] = value
            assign_values(n, q, grid, pos + 1, results)
            grid[row][col] = -1  # Backtrack

def count(n, q):
    results = []
    grid = [[-1] * n for _ in range(n)]

    for pos1 in range(n * n):
        for pos2 in range(pos1 + 1, n * n):
            grid_flat = [[-1] * n for _ in range(n)]  # Prepare grid for each (i,j) pair
            grid_flat[divmod(pos1, n)[0]][divmod(pos1, n)[1]] = 0
            grid_flat[divmod(pos2, n)[0]][divmod(pos2, n)[1]] = 0

            assign_values(n, q, grid_flat, 0, results)

    return [len(results) for _ in range(n * n)]  # Example output style

# Example usage
print(count(2, 2))  # Output corresponding to the test case
