
def is_valid(grid, n, row, col, color):
    # Check left and top neighbors
    if col > 0 and grid[row][col - 1] == color:
        return False
    if row > 0 and grid[row - 1][col] == color:
        return False
    return True

def count_colorings(n, q, grid, row, col, count_zeros):
    if row == n:  # Completed filling the grid
        return 1 if count_zeros == 2 else 0

    next_row, next_col = (row, col + 1) if col + 1 < n else (row + 1, 0)

    total = 0
    # Try all colors for the current cell
    for color in range(q):
        if is_valid(grid, n, row, col, color):
            grid[row][col] = color

            if color == 0:
                total += count_colorings(n, q, grid, next_row, next_col, count_zeros + 1)
            else:
                total += count_colorings(n, q, grid, next_row, next_col, count_zeros)

            grid[row][col] = -1  # Reset for backtracking

    return total

def count(n, q):
    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            # Create empty grid initialized with -1
            grid = [[-1] * n for _ in range(n)]
            grid[pos1 // n][pos1 % n] = 0  # Set first position to 0
            grid[pos2 // n][pos2 % n] = 0  # Set second position to 0
            total = count_colorings(n, q, grid, 0, 0, 0)
            result.append(total)

    return result

# Example usage
print(count(2, 2))  # Should match the expected output for (2, 2)
