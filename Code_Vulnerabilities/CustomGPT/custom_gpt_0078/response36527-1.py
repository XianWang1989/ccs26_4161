
def is_valid(grid, x, y, value):
    n = len(grid)
    # Check horizontal and vertical neighbors
    if x > 0 and grid[x-1][y] == value:
        return False
    if y > 0 and grid[x][y-1] == value:
        return False
    if x < n-1 and grid[x+1][y] == value:
        return False
    if y < n-1 and grid[x][y+1] == value:
        return False
    return True

def backtrack(grid, n, q, idx, placements, result):
    if idx == n * n:
        result[0] += 1
        return

    x, y = divmod(idx, n)
    for value in range(q):
        if is_valid(grid, x, y, value):
            grid[x][y] = value
            backtrack(grid, n, q, idx + 1, placements, result)
            grid[x][y] = -1  # Reset state

def count(n, q):
    result = [0]
    # Start with a grid filled with -1 (unassigned)
    grid = [[-1]*n for _ in range(n)]

    # Iterate over all pairs (i, j) and (k, l)
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            if pos1 == pos2: continue  # Skip same positions

            # Set (i, j) and (k, l) to 0
            i, j = divmod(pos1, n)
            k, l = divmod(pos2, n)
            grid[i][j] = 0
            grid[k][l] = 0

            backtrack(grid, n, q, 0, [], result)

            # Reset the grid for the next iteration
            grid[i][j] = -1
            grid[k][l] = -1

    return result[0]

# Example usage
assert count(2, 2) == 4  # Expected output
