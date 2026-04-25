
def count(n, q):
    def dp(mask, row, col, num_zeros):
        if row == n:
            return 1 if num_zeros == 2 else 0
        if col == n:
            return dp(0, row + 1, 0, num_zeros)

        total = 0
        for value in range(q):
            if (mask & (1 << value)) == 0:  # Ensure no adjacent conflict
                new_mask = mask
                if row > 0:  # Check top cell
                    top_value = grid[row - 1][col]
                    if top_value == value:
                        continue
                if col > 0:  # Check left cell
                    left_value = grid[row][col - 1]
                    if left_value == value:
                        continue

                # Place the value and update grid
                grid[row][col] = value
                if value == 0:
                    total += dp(new_mask | (1 << value), row, col + 1, num_zeros + 1)
                else:
                    total += dp(new_mask | (1 << value), row, col + 1, num_zeros)

        return total

    grid = [[-1] * n for _ in range(n)]  # Initialize grid with -1
    results = []

    for pos1 in range(n*n):
        for pos2 in range(n*n):
            grid = [[-1] * n for _ in range(n)]  # Reset grid for each combination
            grid[pos1 // n][pos1 % n] = 0  # Set first fixed position to 0
            grid[pos2 // n][pos2 % n] = 0  # Set second fixed position to 0
            total_valid = dp(0, 0, 0, 0)
            results.append(total_valid)

    return results

# Example Assertion
assert count(2, 2) == [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
