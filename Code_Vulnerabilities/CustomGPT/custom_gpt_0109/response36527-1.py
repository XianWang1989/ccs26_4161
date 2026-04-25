
def is_valid(grid, row, col, value):
    # Check neighbors
    if row > 0 and grid[row - 1][col] == value: return False  # above
    if row < len(grid) - 1 and grid[row + 1][col] == value: return False  # below
    if col > 0 and grid[row][col - 1] == value: return False  # left
    if col < len(grid) - 1 and grid[row][col + 1] == value: return False  # right
    return True

def backtrack(grid, n, q, pos, count):
    if pos == n * n:
        return count + 1  # found a valid grid configuration

    row, col = divmod(pos, n)
    for value in range(q):
        if (row, col) in [(0, 0), (k, l)] or (row, col) != (0, 0):
            if is_valid(grid, row, col, value):
                grid[row][col] = value
                count = backtrack(grid, n, q, pos + 1, count)
                grid[row][col] = -1  # backtrack

    return count

def count_configurations(n, q):
    result = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    grid = [[-1] * n for _ in range(n)]
                    grid[i][j] = 0  # assign first fixed position
                    grid[k][l] = 0  # assign second fixed position
                    total = backtrack(grid, n, q, 0, 0)
                    result.append(total)
    return result

# Example usage
n = 2
q = 2
print(count_configurations(n, q))  # Output the result for grid of size n with q colors
