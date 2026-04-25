
def is_valid(grid, n, r, c, value):
    # Check left, right, top, bottom for adjacency
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == value:
            return False
    return True

def backtrack(grid, n, q, index, zeros):
    if index == n * n:
        return 1

    r, c = divmod(index, n)

    if (r, c) in zeros:  # If this position must be zero
        grid[r][c] = 0
        return backtrack(grid, n, q, index + 1, zeros)

    total = 0
    for value in range(q):
        if is_valid(grid, n, r, c, value):
            grid[r][c] = value
            total += backtrack(grid, n, q, index + 1, zeros)
            grid[r][c] = -1  # Reset for backtracking

    return total

def count(n, q):
    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            if pos1 == pos2:  # Skip if both positions are the same
                result.append(0)
                continue

            zeros = {divmod(pos1, n), divmod(pos2, n)}
            grid = [[-1 for _ in range(n)] for _ in range(n)]
            total = backtrack(grid, n, q, 0, zeros)
            result.append(total)

    return result

# Example usage
print(count(2, 2))  # Example output
