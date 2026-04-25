
def is_valid(grid, r, c, value, n):
    # Check left and above neighbors
    if c > 0 and grid[r][c-1] == value:
        return False
    if r > 0 and grid[r-1][c] == value:
        return False
    return True

def backtrack(grid, r, c, n, q, i, j):
    # If we reached the end of the grid, all checks passed
    if r == n:
        return 1

    # Move to the next cell
    next_r, next_c = (r, c + 1) if c + 1 < n else (r + 1, 0)

    count = 0
    for value in range(q):
        # Set the cell
        grid[r][c] = value

        # If we are at the fixed positions for zeroes
        if (r, c) == (i, j) or (r, c) == (i, j):
            if grid[i][j] == 0:
                count += backtrack(grid, next_r, next_c, n, q, i, j)
        else:
            if is_valid(grid, r, c, value, n):
                count += backtrack(grid, next_r, next_c, n, q, i, j)

    grid[r][c] = -1  # Reset cell
    return count

def count(n, q):
    result = []
    for i in range(n):
        for j in range(n):
            grid = [[-1] * n for _ in range(n)]
            zero_count = backtrack(grid, 0, 0, n, q, i, j)
            result.append(zero_count)
    return result

# Example usage
print(count(2, 2))  # Example output for a 2x2 grid with 2 colors
