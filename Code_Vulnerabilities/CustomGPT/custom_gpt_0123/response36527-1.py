
def is_valid(grid, row, col, value):
    # Check for vertical and horizontal neighbors
    for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + d_row, col + d_col
        if 0 <= r < len(grid) and 0 <= c < len(grid):
            if grid[r][c] == value:
                return False
    return True

def backtrack(grid, n, q, pos, positions_with_zeros):
    if pos == n * n:
        return 1 if all(grid[r][c] == 0 for r, c in positions_with_zeros) else 0

    row, col = divmod(pos, n)
    total_count = 0

    # Try all possible values for the current position
    for value in range(q):
        if is_valid(grid, row, col, value):
            grid[row][col] = value
            total_count += backtrack(grid, n, q, pos + 1, positions_with_zeros)
            grid[row][col] = -1  # Reset state

    return total_count

def count(n, q):
    results = []

    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:  # Don't count the same position
                results.append(0)
                continue

            grid = [[-1] * n for _ in range(n)]  # -1 represents unassigned
            positions_with_zeros = [(pos1 // n, pos1 % n), (pos2 // n, pos2 % n)]
            grid[positions_with_zeros[0][0]][positions_with_zeros[0][1]] = 0
            grid[positions_with_zeros[1][0]][positions_with_zeros[1][1]] = 0
            count_val = backtrack(grid, n, q, 0, positions_with_zeros)
            results.append(count_val)

    return results

# Example usage
assert count(2, 2) == [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
