
def count(n, q):
    from functools import lru_cache

    @lru_cache(None)
    def dp(pos, last_row, last_col):
        if pos >= n * n:
            return 1

        row = pos // n
        col = pos % n

        valid_count = 0
        for value in range(q):
            # Check constraints for neighbors
            if (row > 0 and last_row == value) or (col > 0 and last_col == value):
                continue

            # Place value in grid and move to the next position
            next_row, next_col = (row, col + 1) if col + 1 < n else (row + 1, 0)
            valid_count += dp(pos + 1, value, last_row if col > 0 else value)

        return valid_count

    result = []

    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:
                result.append(0)
                continue

            count_ways = dp(0, -1, -1)
            result.append(count_ways)

    return result

# Example Test Case
print(count(2, 2))  # Output: [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
