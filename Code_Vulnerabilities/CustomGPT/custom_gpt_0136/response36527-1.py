
def count_assignments(n, q):
    from functools import lru_cache

    # Memoization to store computed results
    @lru_cache(None)
    def dp(row, col, prev1, prev2):
        # Base case: if we've filled all columns in the last row
        if row == n:
            return 1
        if col == n:
            return dp(row + 1, 0, -1, -1)

        total = 0
        for val in range(q):
            # Check for the neighbor constraints
            if (val != prev1) and (val != prev2):
                total += dp(row, col + 1, val, prev1)

        return total

    results = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:  # Skip same positions
                results.append(0)
                continue

            # Flatten the 2D positions
            (i, j) = (pos1 // n, pos1 % n)
            (k, l) = (pos2 // n, pos2 % n)

            count = dp(0, 0, -1, -1)
            results.append(count)

    return results

# Example usage
print(count_assignments(2, 2))
