
def count_ways(n, q):
    from functools import lru_cache

    @lru_cache(None)
    def dp(row, prev_mask, zeros):
        if row == n:  # All rows filled
            return 1

        total_ways = 0
        for mask in range(q ** n):
            if is_valid(mask, prev_mask, zeros, row, n, q):
                total_ways += dp(row + 1, mask, zeros)

        return total_ways

    def is_valid(mask, prev_mask, zeros, row, n, q):
        chosen_values = []
        for j in range(n):
            val = (mask // (q ** j)) % q
            chosen_values.append(val)
            if (row, j) in zeros or (row - 1, j) in zeros:
                if val != 0:
                    return False

            # Check adjacent cells in the previous row
            if row > 0:
                above_val = (prev_mask // (q ** j)) % q
                if val == above_val:
                    return False
                if j > 0:
                    left_val = (prev_mask // (q ** (j - 1))) % q
                    if val == left_val:
                        return False
                if j < n - 1:
                    right_val = (prev_mask // (q ** (j + 1))) % q
                    if val == right_val:
                        return False

        return True

    results = []
    for i in range(n ** 2):
        for j in range(n ** 2):
            zeros = {(i // n, i % n), (j // n, j % n)}
            total = dp(0, 0, zeros)
            results.append(total)

    return results

# Example usage
print(count_ways(2, 2))
