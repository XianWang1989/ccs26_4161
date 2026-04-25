
def count(n, q):
    from itertools import product

    # Precompute valid row configurations
    valid_rows = []
    for row in product(range(q), repeat=n):
        if all(row[i] != row[i + 1] for i in range(n - 1)):
            valid_rows.append(row)

    # Initialize the DP table
    dp = [[0] * len(valid_rows) for _ in range(n)]

    # Fill the first row possibilities
    for j in range(len(valid_rows)):
        dp[0][j] = 1

    # Check row compatibility
    def is_compatible(row1, row2):
        for k in range(n):
            if row1[k] == row2[k]:
                return False
        return True

    # Fill DP table for subsequent rows
    for i in range(1, n):
        for j in range(len(valid_rows)):  # Current row
            for k in range(len(valid_rows)):  # Previous row
                if is_compatible(valid_rows[j], valid_rows[k]):
                    dp[i][j] += dp[i - 1][k]

    # Count configurations based on positions
    results = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            count = 0

            row1, col1 = divmod(pos1, n)
            row2, col2 = divmod(pos2, n)

            for j in range(len(valid_rows)):
                if valid_rows[j][col1] == 0 and valid_rows[j][col2] == 0:
                    count += dp[n - 1][j]

            results.append(count)

    return results

# Example usage
print(count(2, 2))  # Output for n=2 and q=2
