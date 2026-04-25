
def count_valid_assignments(n, q):
    from itertools import product

    # Store results for (row, last value, position of 0, which 0)
    memo = {}

    def is_valid(grid, r, c):
        """ Check if the latest cell (grid[r][c]) is valid against its neighbors. """
        current_value = grid[r][c]
        if r > 0 and grid[r-1][c] == current_value:
            return False
        if c > 0 and grid[r][c-1] == current_value:
            return False
        return True

    def dp(row, prev_row, count_zeros):
        """ Recursive function to build rows of the grid and count valid configurations. """
        if row == n:
            return 1 if count_zeros == 2 else 0

        grid = [prev_row[:] for _ in range(n)]  # Copy the previous row
        total_ways = 0

        for values in product(range(q), repeat=n):
            # Apply values to current row
            grid[row] = values

            # Ensure that the current row is valid
            if all(is_valid(grid, row, col) for col in range(n)):
                # Count zeros in this configuration
                zero_positions = [(row, col) for col in range(n) if values[col] == 0]

                if len(zero_positions) == 2:
                    total_ways += dp(row + 1, grid[row], count_zeros + 2)  # Move to the next row
                elif len(zero_positions) == 1:
                    total_ways += dp(row + 1, grid[row], count_zeros + 1)  # One zero positioned
                else:
                    total_ways += dp(row + 1, grid[row], count_zeros)  # No zero in this row

        return total_ways

    result = []
    for first_zero in range(n * n):
        for second_zero in range(n * n):
            if first_zero != second_zero:
                result.append(dp(0, [0] * n, 0))

    return result

# Test the function with n=2 and q=2
print(count_valid_assignments(2, 2))
