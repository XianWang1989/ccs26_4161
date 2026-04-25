
def count_arrangements(n, q):
    # Dynamic Programming (dp) table to store valid configurations
    dp = [[0] * (1 << n) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case

    for row in range(n):
        for mask in range(1 << n):
            if dp[row][mask] == 0:
                continue  # No arrangements from this state

            for new_mask in range(1 << n):
                # Verify constraints: no adjacent cells have the same value
                valid = True
                for col in range(n):
                    if (new_mask & (1 << col)) and (mask & (1 << col)):
                        valid = False
                        break
                    if col > 0 and (new_mask & (1 << col)) and (new_mask & (1 << (col - 1))):
                        valid = False
                        break

                # If the new mask is valid, propagate the count
                if valid:
                    dp[row + 1][new_mask] += dp[row][mask]

    # Counting configurations with zeros in specified positions
    result = []
    for pos1 in range(n**2):
        for pos2 in range(pos1 + 1, n**2):
            total = 0
            row1, col1 = divmod(pos1, n)
            row2, col2 = divmod(pos2, n)

            for mask in range(1 << n):
                if dp[n][mask] > 0:
                    # Check if positions (row1, col1) and (row2, col2) can be zeros
                    if (mask & (1 << col1)) == 0 and (mask & (1 << col2)) == 0:
                        total += dp[n][mask]

            result.append(total)

    return result

# Example usage
print(count_arrangements(2, 2))  # Replace with desired values of n and q
