
def is_valid(grid, r, c, value):
    # Check left
    if c > 0 and grid[r][c - 1] == value:
        return False
    # Check right
    if c < len(grid) - 1 and grid[r][c + 1] == value:
        return False
    # Check top
    if r > 0 and grid[r - 1][c] == value:
        return False
    # Check bottom
    if r < len(grid) - 1 and grid[r + 1][c] == value:
        return False
    return True

def backtrack(grid, pos, n, q, i, j, k, l, counts):
    if pos == n * n:
        if grid[i][j] == 0 and grid[k][l] == 0:
            counts[0] += 1
        return

    r, c = divmod(pos, n)

    for value in range(q):
        if is_valid(grid, r, c, value):
            grid[r][c] = value
            backtrack(grid, pos + 1, n, q, i, j, k, l, counts)
            grid[r][c] = -1  # Reset back to unvisited

def count(n, q):
    result = []
    grid = [[-1] * n for _ in range(n)]

    # Check all positions (i, j) for first 0
    for i in range(n):
        for j in range(n):
            # Check all positions (k, l) for second 0
            for k in range(n):
                for l in range(n):
                    if (i, j) != (k, l):  # Ensure distinct positions
                        counts = [0]  # Use list to accumulate count as reference
                        backtrack(grid, 0, n, q, i, j, k, l, counts)
                        result.append(counts[0])

    return result

# Example usage
print(count(2, 2))  # This should give you the expected outcome
