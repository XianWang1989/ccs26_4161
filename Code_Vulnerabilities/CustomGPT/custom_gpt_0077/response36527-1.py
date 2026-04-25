
def is_valid(grid, n, r, c, value):
    # Check left
    if c > 0 and grid[r][c - 1] == value:
        return False
    # Check top
    if r > 0 and grid[r - 1][c] == value:
        return False
    return True

def backtrack(grid, n, q, row):
    if row == n:
        return 1

    total = 0
    for value in range(q):
        valid = True
        for col in range(n):
            if grid[row][col] == -1 and is_valid(grid, row, col, value):
                grid[row][col] = value
                total += backtrack(grid, n, q, row + 1)
                grid[row][col] = -1  # Backtrack

    return total

def count(n, q):
    result = []
    for pos1 in range(n*n):
        for pos2 in range(pos1 + 1, n*n):
            grid = [[-1] * n for _ in range(n)]  # Initialize grid
            # Set positions (i, j) and (k, l) to 0
            grid[pos1 // n][pos1 % n] = 0
            grid[pos2 // n][pos2 % n] = 0
            total_ways = backtrack(grid, n, q, 0)
            result.append(total_ways)

    return result

# Example assertion
print(count(2, 2))
