
def is_valid(grid, n, row, col, value):
    # Check neighbors
    if row > 0 and grid[row - 1][col] == value:  # above
        return False
    if row < n - 1 and grid[row + 1][col] == value:  # below
        return False
    if col > 0 and grid[row][col - 1] == value:  # left
        return False
    if col < n - 1 and grid[row][col + 1] == value:  # right
        return False
    return True

def count_assignments(grid, n, q, idx, mask1, mask2):
    if idx == n * n:
        # All cells checked, count this configuration
        return 1 if mask1 == 0 and mask2 == 0 else 0

    row, col = divmod(idx, n)
    total = 0

    for value in range(q):
        if is_valid(grid, n, row, col, value):
            grid[row][col] = value
            total += count_assignments(grid, n, q, idx + 1, mask1, mask2)
            grid[row][col] = -1  # Reset cell

    return total

def count(n, q):
    result = []

    for pos1 in range(n**2):
        for pos2 in range(n**2):
            grid = [[-1 for _ in range(n)] for _ in range(n)]
            grid[pos1 // n][pos1 % n] = 0  # Assign the first position to 0
            grid[pos2 // n][pos2 % n] = 0  # Assign the second position to 0
            total_count = count_assignments(grid, n, q, 0, pos1, pos2)
            result.append(total_count)

    return result

# Example usage
print(count(2, 2))
