
def is_valid(grid, n, row, col, value):
    # Check if value can be placed at (row, col)
    if (row > 0 and grid[row - 1][col] == value) or \
       (col > 0 and grid[row][col - 1] == value) or \
       (row < n - 1 and grid[row + 1][col] == value) or \
       (col < n - 1 and grid[row][col + 1] == value):
        return False
    return True

def count_arrangements(n, q, pos1, pos2):
    # Grid initialization
    grid = [[-1] * n for _ in range(n)]
    grid[pos1 // n][pos1 % n] = 0
    grid[pos2 // n][pos2 % n] = 0

    memo = {}

    def dp(row, col):
        if row == n:  # Finished filling the grid
            return 1
        if col == n:  # Move to next row
            return dp(row + 1, 0)

        key = (row, col, tuple(tuple(r) for r in grid))
        if key in memo:
            return memo[key]

        total_count = 0
        for value in range(q):
            if (row * n + col not in (pos1, pos2)) and is_valid(grid, n, row, col, value):
                grid[row][col] = value
                total_count += dp(row, col + 1)
                grid[row][col] = -1  # Reset for backtracking

        memo[key] = total_count
        return total_count

    return dp(0, 0)

def count(n, q):
    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 != pos2:
                result.append(count_arrangements(n, q, pos1, pos2))
            else:
                result.append(0)  # Same positions not allowed
    return result

# Example usage
print(count(2, 2))  # Output for 2x2 grid with 2 values
