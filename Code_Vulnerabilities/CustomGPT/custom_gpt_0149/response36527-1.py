
def is_valid(grid, n, row, col, value):
    # Check adjacent cells
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc
        if 0 <= r < n and 0 <= c < n and grid[r][c] == value:
            return False
    return True

def count_ways(n, q, fixed_positions):
    count = 0
    total_cells = n * n

    def backtrack(cell_index, grid):
        nonlocal count
        if cell_index == total_cells:
            count += 1
            return

        row, col = divmod(cell_index, n)
        if (row, col) in fixed_positions:
            backtrack(cell_index + 1, grid)
        else:
            for value in range(q):
                if is_valid(grid, n, row, col, value):
                    grid[row][col] = value
                    backtrack(cell_index + 1, grid)
                    grid[row][col] = -1  # Reset

    grid = [[-1] * n for _ in range(n)]  # Initialize grid with -1
    for (i, j) in fixed_positions:
        grid[i][j] = 0  # Set fixed positions to 0

    backtrack(0, grid)
    return count

def count_all(n, q):
    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            if pos1 != pos2:  # Ensure positions are different
                fixed_positions = [(divmod(pos1, n)), (divmod(pos2, n))]
                total_count = count_ways(n, q, fixed_positions)
                result.append(total_count)
    return result

# Example usage
result = count_all(2, 2)
print(result)  # Output for n=2, q=2
