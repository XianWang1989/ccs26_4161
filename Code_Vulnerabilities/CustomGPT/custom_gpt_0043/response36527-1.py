
def is_valid(grid, row, col, value):
    # Check left and right
    if col > 0 and grid[row][col - 1] == value:
        return False
    if col < len(grid) - 1 and grid[row][col + 1] == value:
        return False
    # Check up and down
    if row > 0 and grid[row - 1][col] == value:
        return False
    if row < len(grid) - 1 and grid[row + 1][col] == value:
        return False
    return True

def backtrack(grid, positions, q, index, results):
    if index == len(positions):
        # Count valid configurations for the current grid
        count = 1
        for r in range(len(grid)):
            for c in range(len(grid)):
                if (r * len(grid) + c) in positions:
                    if grid[r][c] != 0:
                        count = 0
        results.append(count)
        return

    # Get the next position to fill
    r, c = positions[index]

    for value in range(q):
        if is_valid(grid, r, c, value):
            grid[r][c] = value
            backtrack(grid, positions, q, index + 1, results)
            grid[r][c] = -1  # reset for backtracking

def count_valid_assignments(n, q):
    results = []
    grid = [[-1] * n for _ in range(n)]
    positions = [(i, j) for i in range(n) for j in range(n)]
    for i in range(n ** 2):
        for j in range(i + 1, n ** 2):
            grid[i // n][i % n] = 0  # Assign first zero
            grid[j // n][j % n] = 0  # Assign second zero
            backtrack(grid, positions, q, 0, results)
            grid[i // n][i % n] = -1  # unassign for backtracking
            grid[j // n][j % n] = -1  # unassign for backtracking
    return results

# Example usage
n = 2
q = 2
output = count_valid_assignments(n, q)
print(output)
