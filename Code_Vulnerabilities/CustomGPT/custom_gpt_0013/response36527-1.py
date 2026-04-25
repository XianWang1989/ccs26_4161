
def count(n, q):
    # DP table: dp[mask] stores the number of valid ways to fill the row with given mask
    dp = [[0] * (1 << n) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: 1 way to fill 0 rows

    # Iterate through each row
    for i in range(n):
        # Iterate through all possible masks for current row
        for mask in range(1 << n):
            # Check how many ways can we assign colors to the current row
            if dp[i][mask] == 0:  # No valid way to fill this row
                continue

            # Try to fill the next row
            for next_mask in range(1 << n):
                if not is_valid(mask, next_mask, n):
                    continue
                # Count the valid configurations
                dp[i + 1][next_mask] += dp[i][mask]

    # Total combinations for all valid configurations
    result = []
    for pos1 in range(n ** 2):
        for pos2 in range(n ** 2):
            total = 0
            for mask in range(1 << n):
                if bin(mask).count('0') == 1:  # Ensure at least one '0' for position checks
                    total += dp[n][mask]  # Add valid ways for final row
            result.append(total)

    return result

def is_valid(current_mask, next_mask, n):
    # Check if next_mask is valid in terms of adjacent colors
    for j in range(n):
        if (next_mask & (1 << j)) != 0:  # If current cell (j) is filled
            # Check horizontal constraint
            if j > 0 and (current_mask & (1 << (j - 1))) == (1 << (j - 1)):
                return False
            if j < n - 1 and (current_mask & (1 << (j + 1))) == (1 << (j + 1)):
                return False
    return True

# Example Usage
print(count(2, 2))  # Example call, results may vary based on the specific constraints
