
def is_valid(grid, n, row, col, value):
    # Check the left neighbor
    if col > 0 and grid[row][col - 1] == value:
        return False
    # Check the right neighbor
    if col < n - 1 and grid[row][col + 1] == value:
        return False
    # Check the top neighbor
    if row > 0 and grid[row - 1][col] == value:
        return False
    # Check the bottom neighbor
    if row < n - 1 and grid[row + 1][col] == value:
        return False
    return True

def count_ways(grid, n, q, pos1, pos2, i, j):
    if i == n:  # We've filled the whole grid
        return 1

    next_i, next_j = (i, j + 1) if j + 1 < n else (i + 1, 0)
    total_ways = 0

    for value in range(q):  # Trying all values from 0 to q-1
        if (i, j) == pos1 or (i, j) == pos2:
            current_value = 0  # Forces these positions to 0
        else:
            current_value = value

        if is_valid(grid, n, i, j, current_value):
            grid[i][j] = current_value
            total_ways += count_ways(grid, n, q, pos1, pos2, next_i, next_j)
            grid[i][j] = -1  # Reset to -1 for backtracking

    return total_ways

def count(n, q):
    results = []
    for pos1 in range(n ** 2):
        for pos2 in range(n ** 2):
            if pos1 == pos2:
                results.append(0)  # Skip same position
                continue

            grid = [[-1] * n for _ in range(n)]  # Initialize grid with -1
            row1, col1 = divmod(pos1, n)
            row2, col2 = divmod(pos2, n)
            total_count = count_ways(grid, n, q, (row1, col1), (row2, col2), 0, 0)
            results.append(total_count)

    return results

# Example test
print(count(2, 2))
