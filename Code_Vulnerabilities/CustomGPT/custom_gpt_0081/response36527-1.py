
def is_valid(row, last_color, n):
    # Check if this row is valid with respect to the last row's colors
    for c in range(n):
        if c > 0 and row[c] == row[c - 1]:  # Check left neighbor
            return False
        if c > 0 and last_color[c] == row[c]:  # Check above neighbor
            return False
    return True

def fill_grid(n, q):
    # This will store the number of ways to fill the grid
    dp = [[0] * (1 << (n * 2)) for _ in range(n + 1)]

    # Fill the dp array for each row
    for i in range(n + 1):
        for mask in range(1 << (n * 2)):
            dp[i][mask] = 0

    dp[0][0] = 1  # Base case: 1 way to fill 0 rows with 0 colors

    for row in range(n):
        for mask in range(1 << (n * 2)):
            if dp[row][mask] == 0:
                continue

            for color in range(q):
                for position in range(n):
                    # Build new mask for this row
                    new_mask = mask | (color << (2 * position))
                    if is_valid(new_mask, (mask >> (2 * position)) & 0b11, n):
                        dp[row + 1][new_mask] += dp[row][mask]

    return dp[n]

def count_ways(n, q):
    result = []
    for i in range(n * n):
        for j in range(i + 1, n * n):
            total = 0
            # For each pair (i, j), count configurations with these filled with 0
            for mask in range(1 << (n * n)):
                if (mask & (1 << i)) and (mask & (1 << j)):
                    count = fill_grid(n, q)  # Call function to fill the grid
                    total += count  # Add valid counts
            result.append(total)
    return result

# For example
n = 2
q = 2
result = count_ways(n, q)
print(result)
