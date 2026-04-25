
def can_place(value, grid, row, col):
    # Check left, right, up, down for the same value
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid) and grid[r][c] == value:
            return False
    return True

def backtrack(grid, positions, idx, n, q, results):
    if idx == len(positions):
        # All positions filled correctly, count valid assignment
        count = sum(1 for row in grid for val in row if val == 0)
        results.append(count)
        return

    i, j = positions[idx]
    for value in range(q):
        if can_place(value, grid, i, j):
            grid[i][j] = value
            backtrack(grid, positions, idx + 1, n, q, results)
            grid[i][j] = -1  # Reset the position

def count_assignments(n, q):
    positions = [(i, j) for i in range(n) for j in range(n)]
    results = []
    grid = [[-1] * n for _ in range(n)]  # -1 indicates unassigned
    backtrack(grid, positions, 0, n, q, results)
    return results

# Example usage
n = 2
q = 2
print(count_assignments(n, q))
