
def count(n, q):
    # Create a memoization dictionary
    memo = {}

    def dp(row, mask1, mask2):
        if row == n:  # All rows filled
            return 1

        if (row, mask1, mask2) in memo:
            return memo[(row, mask1, mask2)]

        # Count valid configurations for the next row
        total = 0
        for next_mask in range(q**n):
            # Ensure no two adjacent cells are the same
            valid = True
            for col in range(n):
                if (next_mask // (q ** col)) % q == (mask1 // (q ** col)) % q:  # Same column
                    valid = False
                    break
                if col > 0 and (next_mask // (q ** (col - 1))) % q == (next_mask // (q ** col)) % q:  # Adjacent column
                    valid = False
                    break
            if not valid:
                continue

            total += dp(row + 1, next_mask, mask1)

        memo[(row, mask1, mask2)] = total
        return total

    results = []

    # Loop through all positions for placing zeros
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:  # Both cannot be the same position
                results.append(0)
                continue

            # Initiate the state for the first row
            results.append(dp(0, 0, 0))

    return results

# Example usage
print(count(2, 2))  # Output for the given example
