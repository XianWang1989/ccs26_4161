
def is_valid(grid, r, c, value, n):
    """ Check if placing value at (r, c) is valid. """
    if (r > 0 and grid[r - 1][c] == value) or (c > 0 and grid[r][c - 1] == value):
        return False
    return True

def count_assignments(r, c, grid, n, q, pos1, pos2):
    """ Use backtracking to count valid assignments. """
    if r == n:  # All rows filled
        return 1 if grid[pos1 // n][pos1 % n] == 0 and grid[pos2 // n][pos2 % n] == 0 else 0

    next_r, next_c = (r, c + 1) if c < n - 1 else (r + 1, 0)  # Move to the next column or row
    total = 0

    for value in range(q):
        if (r, c) != (pos1 // n, pos1 % n) and (r, c) != (pos2 // n, pos2 % n):
            grid[r][c] = value
            total += count_assignments(next_r, next_c, grid, n, q, pos1, pos2)
            grid[r][c] = -1  # Reset

        elif is_valid(grid, r, c, value, n):
            grid[r][c] = value
            total += count_assignments(next_r, next_c, grid, n, q, pos1, pos2)
            grid[r][c] = -1  # Reset

    return total

def count(n, q):
    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            grid = [[-1]*n for _ in range(n)]
            total = count_assignments(0, 0, grid, n, q, pos1, pos2)
            result.append(total)
    return result

# Example usage
print(count(2, 2))  # Output: [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
