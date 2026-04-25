
def count(n, q):
    from functools import lru_cache

    @lru_cache(None)
    def valid(mask1, mask2):
        """ Check if two row masks are valid adjacent. """
        return not (mask1 & mask2)

    def generate_masks(row):
        """ Generate all valid masks for a row. """
        masks = []
        for mask in range(1 << q):
            if bin(mask).count('1') == row:
                masks.append(mask)
        return masks

    # DP table to store counts
    dp = [[0] * (1 << q) for _ in range(n)]
    for mask in range(1 << q):
        dp[0][mask] = 1  # Initialize first row

    for i in range(1, n):
        for mask in range(1 << q):
            for prev_mask in range(1 << q):
                if valid(prev_mask, mask):
                    dp[i][mask] += dp[i - 1][prev_mask]

    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            total = 0
            for mask1 in range(1 << q):
                for mask2 in range(1 << q):
                    valid_count = dp[n-1][mask1] * dp[n-1][mask2]  # Total valid for rows
                    # Check if positions pos1 and pos2 are valid
                    if (mask1 & (1 << (pos1 % q))) == 0 and (mask2 & (1 << (pos2 % q))) == 0:
                        total += valid_count

            result.append(total)

    return result

# Example usage
print(count(2, 2))  # Output for n=2, q=2
