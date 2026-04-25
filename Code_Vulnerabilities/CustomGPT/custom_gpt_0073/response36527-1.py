
def count(n, q):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(row, col, left_mask, up_mask):
        if row == n:  # Finished all rows
            return 1

        if col == n:  # Move to the next row
            return dp(row + 1, 0, 0, 0)

        total = 0
        for val in range(q):
            if ((left_mask & (1 << val)) == 0) and ((up_mask & (1 << val)) == 0):  # Valid placement
                total += dp(row, col + 1, (left_mask | (1 << val)), (up_mask | (1 << val)))

        return total

    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            if pos1 == pos2:
                result.append(0)
                continue

            total_count = dp(0, 0, 0, 0)
            result.append(total_count)

    return result

# Example usage:
print(count(2, 2))
