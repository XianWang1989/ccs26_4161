def count_colorings(n, q):
    # Base case: if n is 0, there's one way to color the grid (doing nothing)
    if n == 0:
        return 1

    # Initialize DP table
    # dp[row][prev_row_colors] represents the number of ways to color up to 'row' rows
    # with 'prev_row_colors' being the coloring of the previous row
    dp = {}

    # Function to check if two rows are compatible
    def are_compatible(row1, row2):
        for col in range(n):
            if row1[col] == row2[col]:
                return False
        return True

    # Function to generate all valid colorings for a row
    def generate_valid_rows():
        from itertools import product
        all_rows = product(range(q), repeat=n)
        return [row for row in all_rows if all(row[i] != row[i+1] for i in range(n-1))]

    valid_rows = generate_valid_rows()

    # Initialize the first row possibilities
    for row in valid_rows:
        dp[(0, row)] = 1

    # Fill DP table
    for row_idx in range(1, n):
        for current_row in valid_rows:
            dp[(row_idx, current_row)] = 0
            for prev_row in valid_rows:
                if are_compatible(prev_row, current_row):
                    dp[(row_idx, current_row)] += dp.get((row_idx - 1, prev_row), 0)

    # Sum up all valid colorings for the last row
    total_colorings = sum(dp.get((n - 1, row), 0) for row in valid_rows)
    return total_colorings

# Example usage:
n = 4  # Grid size
q = 3  # Number of colors
print(count_colorings(n, q))
