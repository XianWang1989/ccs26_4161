
def count_valid_colorings(n, q):
    # dp[mask][r] -> number of valid configurations of the first r rows where the last row is `mask`
    dp = [[0] * (n + 1) for _ in range(1 << (n))]
    # Initialize dp for the first row
    for mask in range(1 << n):
        if is_valid(mask, n):
            dp[mask][1] += 1

    # Fill dp for remaining rows
    for r in range(1, n):
        for mask in range(1 << n):
            if dp[mask][r] > 0:  # If there's a valid configuration
                for next_mask in range(1 << n):
                    if is_valid_next(mask, next_mask, n):
                        dp[next_mask][r + 1] += dp[mask][r]

    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 != pos2:
                result.append(count_ways_with_zeros(dp, n, q, pos1, pos2))

    return result

def is_valid(mask, n):
    # Check if the mask is valid
    for i in range(n):
        if i > 0 and (mask & (1 << i)) == (mask & (1 << (i - 1))):
            return False
    return True

def is_valid_next(last_mask, next_mask, n):
    # Check if the next row's mask is valid against the last row
    for i in range(n):
        if (i > 0 and (next_mask & (1 << i)) == (next_mask & (1 << (i - 1)))) or \
           ((last_mask & (1 << i)) == (next_mask & (1 << i))):
            return False
    return True

def count_ways_with_zeros(dp, n, q, pos1, pos2):
    total = 0
    for mask in range(1 << n):
        for r in range(1, n + 1):
            zero_pos1 = pos1 // n == r - 1 and mask & (1 << (pos1 % n)) == 0
            zero_pos2 = pos2 // n == r - 1 and mask & (1 << (pos2 % n)) == 0
            if zero_pos1 and zero_pos2:
                total += dp[mask][r]
    return total

# Example usage
print(count_valid_colorings(2, 2))
