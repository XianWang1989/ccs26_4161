
def is_valid(grid, r, c, n):
    # Check for neighbors
    value = grid[r][c]
    if r > 0 and grid[r - 1][c] == value:
        return False
    if r < n - 1 and grid[r + 1][c] == value:
        return False
    if c > 0 and grid[r][c - 1] == value:
        return False
    if c < n - 1 and grid[r][c + 1] == value:
        return False
    return True

def count_configurations(grid, n, q, idx):
    if idx == n * n:
        return 1  # Valid configuration found
    total = 0
    r, c = divmod(idx, n)
    for value in range(q):
        grid[r][c] = value
        if is_valid(grid, r, c, n):
            total += count_configurations(grid, n, q, idx + 1)
    grid[r][c] = -1  # Reset to -1 (unassigned)
    return total

def count(n, q):
    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:
                result.append(0)  # Cannot assign the same position
                continue
            total = 0
            for value in range(q):
                grid = [[-1] * n for _ in range(n)]  # Initialize grid
                grid[divmod(pos1, n)[0]][divmod(pos1, n)[1]] = 0
                grid[divmod(pos2, n)[0]][divmod(pos2, n)[1]] = 0
                total += count_configurations(grid, n, q, 0)
            result.append(total)
    return result

assert count(2, 2) == [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
