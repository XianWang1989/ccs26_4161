
def is_valid(grid, row, col, value):
    # Check the current cell's neighbors
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = row + dx, col + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[nx][ny] == value:
            return False
    return True

def count_assignments(n, q, positions):
    result = [0] * (n * n)  # Store results for each (i, j, k, l) assignment
    total_cells = n * n

    def backtrack(grid, idx):
        if idx == total_cells:
            # Count valid configurations for each pair of positions
            for (pos1, pos2) in positions:
                if grid[pos1 // n][pos1 % n] == 0 and grid[pos2 // n][pos2 % n] == 0:
                    result[pos1 * total_cells + pos2] += 1
            return

        row, col = idx // n, idx % n
        for value in range(q):
            if is_valid(grid, row, col, value):
                grid[row][col] = value
                backtrack(grid, idx + 1)
                grid[row][col] = -1  # Reset cell after backtracking

    # Initialize grid with -1 (unassigned)
    grid = [[-1] * n for _ in range(n)]
    backtrack(grid, 0)

    return result

# Example usage:
positions = [(0, 1), (1, 0), (2, 3), (3, 2)]  # Example positions (i, j, k, l)
print(count_assignments(2, 2, positions))
