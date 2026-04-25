
def count(n, q):
    # dp[mask] will represent the number of valid grid configurations for a row
    dp = [[0] * (1 << q) for _ in range(n)]

    # Helper function to check if two masks are valid neighbors
    def is_valid(mask1, mask2):
        for j in range(q):
            if (mask1 & (1 << j)) and (mask2 & (1 << j)):
                return False
        return True

    # Initialize the first row
    for mask in range(1 << q):
        dp[0][mask] = 1

    # Fill in the dp table for all rows
    for i in range(1, n):
        for mask in range(1 << q):
            for prev_mask in range(1 << q):
                if is_valid(prev_mask, mask):
                    dp[i][mask] += dp[i - 1][prev_mask]

    # Count valid configurations for each (i, j, k, l)
    result = []
    for pos1 in range(n*n):
        for pos2 in range(n*n):
            total = 0
            # Calculate number of valid configurations
            for mask in range(1 << q):
                if (mask & 1) == 0:  # Ensure (i,j) is 0
                    for next_mask in range(1 << q):
                        if (next_mask & 1) == 0 and is_valid(mask, next_mask):  # Ensure (k,l) is 0
                            total += dp[n-1][next_mask]
            result.append(total)

    return result

# Example usage
print(count(2, 2))
