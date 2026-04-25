
def count_ways(n, q):
    # DP table: dp[mask][i] is the number of ways to fill row `i` with colors represented in `mask`
    dp = [[0] * (1 << q) for _ in range(n)]

    # Precompute valid masks for each previous row
    for mask in range(1 << q):
        is_valid = True
        for j in range(q):
            if (mask & (1 << j)) and (j + 1 < q and (mask & (1 << (j + 1)))):
                is_valid = False
                break
        if is_valid:
            # Fill the first row
            dp[0][mask] = 1

    # Fill the DP table
    for i in range(1, n):
        for mask in range(1 << q):
            if dp[i - 1][mask] > 0:
                for next_mask in range(1 << q):
                    if is_valid_transition(mask, next_mask, q):
                        dp[i][next_mask] += dp[i - 1][mask]

    results = []

    # Count configurations for each (i, j, k, l) where values at positions are 0
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            total = 0
            # Skip if both positions are the same
            if pos1 == pos2:
                continue

            for mask in range(1 << q):
                if (mask & 1) == 0:  # Check if the first color at pos1 is 0
                    if (dp[n - 1][mask] > 0 and (mask & (1 << (pos2 % n))) == 0):
                        total += dp[n - 1][mask]

            results.append(total)

    return results

def is_valid_transition(mask1, mask2, q):
    for j in range(q):
        # Check if two adjacent bits are set in the adjacent rows
        if (mask1 & (1 << j)) and (j + 1 < q and (mask2 & (1 << (j + 1)))):
            return False
    return True

# Example usage
print(count_ways(2, 2))
