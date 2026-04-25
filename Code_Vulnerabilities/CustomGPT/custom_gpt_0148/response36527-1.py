
def is_valid(grid, r, c, n, value):
    # Check adjacent cells to validate current value
    if r > 0 and grid[r - 1][c] == value: return False
    if r < n - 1 and grid[r + 1][c] == value: return False
    if c > 0 and grid[r][c - 1] == value: return False
    if c < n - 1 and grid[r][c + 1] == value: return False
    return True

def count_ways(grid, n, q, pos1, pos2, index):
    if index == n * n:
        return 1 if grid[pos1 // n][pos1 % n] == 0 and grid[pos2 // n][pos2 % n] == 0 else 0

    total = 0
    r, c = divmod(index, n)

    for value in range(q):
        grid[r][c] = value
        if is_valid(grid, r, c, n, value):
            total += count_ways(grid, n, q, pos1, pos2, index + 1)

    grid[r][c] = -1  # Resetting cell
    return total

def count(n, q):
    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            grid = [[-1 for _ in range(n)] for _ in range(n)]
            total = count_ways(grid, n, q, pos1, pos2, 0)
            result.append(total)
    return result

# Example usage
print(count(2, 2))  # Output for the given test case
