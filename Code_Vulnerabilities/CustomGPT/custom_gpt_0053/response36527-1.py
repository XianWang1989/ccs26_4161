
def is_valid(grid, n):
    for r in range(n):
        for c in range(n):
            if r > 0 and grid[r][c] == grid[r - 1][c]:  # Check top
                return False
            if c > 0 and grid[r][c] == grid[r][c - 1]:  # Check left
                return False
    return True

def count_valid_configs(n, q, pos1, pos2, grid, memo):
    grid_tuple = tuple(tuple(row) for row in grid)
    if grid_tuple in memo:
        return memo[grid_tuple]

    if pos1 == n ** 2:
        return 1 if is_valid(grid, n) else 0

    # Proceed to fill the next position
    count = 0
    next_pos = pos1 + 1
    for value in range(q):
        if (pos1 == pos2 and value == 0):  # Ensure position pos2 also gets 0
            continue
        # Determine grid coordinates
        r, c = divmod(pos1, n)
        grid[r][c] = value

        count += count_valid_configs(n, q, next_pos, pos2, grid, memo)

    grid[r][c] = -1  # Reset for the next iteration
    memo[grid_tuple] = count
    return count

def count(n, q):
    result = []
    for pos1 in range(n ** 2):
        for pos2 in range(n ** 2):
            grid = [[-1] * n for _ in range(n)]
            memo = {}
            total = count_valid_configs(n, q, 0, pos1 if pos1 == pos2 else pos2, grid, memo)
            result.append(total)
    return result

# Example usage
print(count(2, 2))  # Output for a 2x2 grid with 2 colors
