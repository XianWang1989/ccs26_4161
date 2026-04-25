
def is_valid(mask, prev_mask, n):
    for j in range(n):
        if (mask & (1 << j)) != 0:  # If j-th bit is set
            if (prev_mask & (1 << j)) != 0:  # Same column as previous
                return False
            if j > 0 and (mask & (1 << (j - 1))) != 0:  # Left neighbor
                return False
            if j < n - 1 and (mask & (1 << (j + 1))) != 0:  # Right neighbor
                return False
    return True

def count(n, q):
    # Create a DP table
    dp = [[0] * (1 << n) for _ in range(n + 1)]
    # Initialize base case
    dp[0][0] = 1  

    for row in range(n):
        for mask in range(1 << n):
            if dp[row][mask] > 0:
                for new_mask in range(1 << n):
                    if is_valid(new_mask, mask, n):  # Check if new_mask is valid with respect to previous row
                        dp[row + 1][new_mask] += dp[row][mask]

    # The final result array to store counts for each pair of fixed positions
    result = [0] * (n * n)

    # Count configurations with 0's in specified positions
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 != pos2:  # Ensure the positions are different
                total = 0
                for mask in range(1 << n):
                    if (mask & (1 << (pos1 % n))) == 0 and (mask & (1 << (pos2 % n))) == 0:
                        total += dp[n][mask]
                result[pos1 * n + pos2] = total

    return result

# Example usage
print(count(2, 2))  # Output should match the expected result
