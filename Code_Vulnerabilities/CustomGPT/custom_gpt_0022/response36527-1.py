
def is_valid(grid, r, c, n, value):
    # Check neighbors
    if r > 0 and grid[r - 1][c] == value: return False
    if r < n - 1 and grid[r + 1][c] == value: return False
    if c > 0 and grid[r][c - 1] == value: return False
    if c < n - 1 and grid[r][c + 1] == value: return False
    return True

def count_assignments(grid, n, q, i, j, used):
    if j == n:
        return count_assignments(grid, n, q, i + 1, 0, used)
    if i == n:
        return 1

    total_count = 0
    for value in range(q):
        if is_valid(grid, i, j, n, value):
            grid[i][j] = value
            total_count += count_assignments(grid, n, q, i, j + 1, used)
            grid[i][j] = -1  # Reset for backtracking

    return total_count

def count(n, q):
    result = []

    for pos1 in range(n**2):
        for pos2 in range(pos1 + 1, n**2):  # Ensure (k,l) is different from (i,j)
            total = 0

            # Initialize grid
            grid = [[-1]*n for _ in range(n)]
            grid[pos1 // n][pos1 % n] = 0
            grid[pos2 // n][pos2 % n] = 0

            total += count_assignments(grid, n, q, 0, 0, set())
            result.append(total)

    return result

# Test case
print(count(2, 2))  # Example output
