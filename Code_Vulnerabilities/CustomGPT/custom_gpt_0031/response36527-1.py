
def is_valid_mask(mask, previous_mask, n, q):
    for i in range(n):
        if (mask & (1 << i)) != 0 and (previous_mask & (1 << i)) != 0:
            return False  # Two adjacent same values
        if i > 0 and (mask & (1 << i)) != 0 and (mask & (1 << (i - 1))) != 0:
            return False  # Same value in the same row
    return True

def count_valid_configurations(n, q):
    dp = [[0] * (1 << n) for _ in range(n + 1)]
    dp[0][0] = 1  # One way to fill 0 rows with empty configuration

    for row in range(n):
        for mask in range(1 << n):
            if dp[row][mask] == 0:
                continue
            # Try to fill the next row
            for new_mask in range(1 << n):
                if is_valid_mask(new_mask, mask, n, q):
                    dp[row + 1][new_mask] += dp[row][mask]

    result = []
    # Calculate based on the two specified positions (0 at (i,j) and (k,l))
    for a in range(n * n):
        for b in range(n * n):
            total = 0
            for mask in range(1 << n):
                if (mask & 1) == 0:  # Position a must be 0
                    total += dp[n][mask]  # Count valid configurations
            result.append(total)

    return result

# Example usage
n = 2
q = 2
print(count_valid_configurations(n, q))  # Output for a 2x2 grid
