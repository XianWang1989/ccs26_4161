
def is_valid(grid, n, row, col, value):
    # Check left, right, top, bottom for adjacency
    if col > 0 and grid[row][col - 1] == value:
        return False
    if col < n - 1 and grid[row][col + 1] == value:
        return False
    if row > 0 and grid[row - 1][col] == value:
        return False
    if row < n - 1 and grid[row + 1][col] == value:
        return False
    return True

def count_configurations(n, q, fixed_positions):
    grid = [[-1] * n for _ in range(n)]  # -1 means unassigned
    result = []

    def backtrack(pos_idx):
        if pos_idx == len(fixed_positions):
            # Check if all positions are filled correctly
            total = 1
            for fixed_pos in fixed_positions:
                grid[fixed_pos[0]][fixed_pos[1]] = 0
            for r in range(n):
                for c in range(n):
                    if grid[r][c] == -1:
                        continue
                    if not is_valid(grid, n, r, c, grid[r][c]):
                        return 0
            return total

        # Place `0` in the fixed position
        row, col = fixed_positions[pos_idx]
        grid[row][col] = 0

        # Call backtrack for the next position
        count = backtrack(pos_idx + 1)

        # Backtrack
        grid[row][col] = -1
        return count

    # Initial fixed positions for (i,j) and (k,l)
    count = backtrack(0)
    result.append(count)

    return result

# Example usage
n = 2
q = 2
fixed_positions = [(0, 0), (1, 1)]  # Example fixed positions (you can change as needed)
print(count_configurations(n, q, fixed_positions))
