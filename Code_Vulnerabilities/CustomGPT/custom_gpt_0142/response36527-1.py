
def is_valid(mask1, mask2, n):
    for i in range(n):
        if (mask1 & (1 << i)) and (mask2 & (1 << i)):
            return False
    return True

def count_colorings(n, q):
    dp = [[0] * (1 << n) for _ in range(n)]

    # Base case: For the first row, all combinations are valid.
    for mask in range(1 << n):
        if valid_mask(mask, n):
            dp[0][mask] = 1

    # Fill dp table
    for r in range(1, n):
        for mask in range(1 << n):
            if not valid_mask(mask, n):
                continue
            for prev_mask in range(1 << n):
                if dp[r-1][prev_mask] > 0 and is_valid(mask, prev_mask, n):
                    dp[r][mask] += dp[r-1][prev_mask]

    # Count valid configurations
    result = []
    for x1 in range(n):
        for y1 in range(n):
            for x2 in range(n):
                for y2 in range(n):
                    if (x1, y1) == (x2, y2):
                        continue
                    total = 0
                    for mask in range(1 << n):
                        if valid_mask(mask, n):
                            total += (dp[n-1][mask] * dp[n-1][mask])  # Each row can independently have valid configurations
                    result.append(total)

    return result

def valid_mask(mask, n):
    for i in range(n):
        if (mask & (1 << i)) and (mask & (1 << (i+1))):
            return False
    return True

# Example usage
print(count_colorings(2, 2))  # Outputs a count of valid configurations based on the criteria
