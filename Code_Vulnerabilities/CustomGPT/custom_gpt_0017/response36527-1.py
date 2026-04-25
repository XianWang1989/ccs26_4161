
def count(n, q):
    # Total number of cells
    total_cells = n * n
    # DP table initialized
    dp = [[[0] * q for _ in range(total_cells)] for _ in range(total_cells + 1)]

    # Base case: No cells assigned
    for i in range(q):
        dp[0][0][i] = 1

    # Fill DP table
    for pos in range(total_cells):
        for mask in range(1 << n):
            for val in range(q):
                if dp[pos][mask][val] > 0:
                    next_pos = pos + 1
                    if next_pos < total_cells:
                        for new_val in range(q):
                            # Check adjacency (last cell of the row)
                            if (mask & (1 << (next_pos % n))) == 0 and (next_pos % n == 0 or new_val != val):
                                new_mask = mask | (1 << (next_pos % n))
                                dp[next_pos][new_mask][new_val] += dp[pos][mask][val]

    result = []
    # Count valid configurations for each pair of positions (i, j)
    for pos1 in range(total_cells):
        for pos2 in range(total_cells):
            if pos1 != pos2:
                count_ways = 0
                for val in range(q):
                    count_ways += dp[total_cells][0][val]  # All ways considering fixed values at pos1 and pos2
                result.append(count_ways)
            else:
                result.append(0)

    return result

# Example usage:
assert count(2, 2) == [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
