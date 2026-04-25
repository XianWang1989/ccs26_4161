
def is_valid_assignment(grid, n, x, y, value):
    # Check neighboring positions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == value:
            return False
    return True

def count_ways(n, q, pos1, pos2):
    grid = [[-1] * n for _ in range(n)]  # -1 indicates unassigned
    return assign(grid, n, q, 0, 0, pos1, pos2)

def assign(grid, n, q, x, y, pos1, pos2):
    if x == n:  # Finished assigning all rows
        return 1  # Valid configuration found

    next_x, next_y = (x, y + 1) if (y + 1) < n else (x + 1, 0)

    count = 0
    for value in range(q):
        if (x * n + y == pos1 or x * n + y == pos2) and value != 0:
            continue  # Ensure (i, j) and (k, l) are zero

        if is_valid_assignment(grid, n, x, y, value):
            grid[x][y] = value  # Assign value
            count += assign(grid, n, q, next_x, next_y, pos1, pos2)  # Recursively assign
            grid[x][y] = -1  # Backtrack

    return count

def compute_counts(n, q):
    results = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:
                results.append(0)  # Same position, invalid
                continue
            total_count = count_ways(n, q, pos1, pos2)
            results.append(total_count)
    return results

# Example usage:
result = compute_counts(2, 2)
print(result)  # Should match the expected output
