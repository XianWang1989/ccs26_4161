
def count_valid_grid_configurations(n, q):
    from functools import lru_cache

    @lru_cache(None)
    def dp(row, mask, prev_mask):
        if row == n:
            return 1
        total = 0
        for next_mask in range(q ** n):
            valid = True
            for col in range(n):
                current_value = (next_mask // (q ** col)) % q
                left_value = (next_mask // (q ** (col - 1))) % q if col > 0 else -1
                above_value = (prev_mask // (q ** col)) % q
                if current_value == left_value or current_value == above_value:
                    valid = False
                    break
            if valid:
                total += dp(row + 1, next_mask, mask)
        return total

    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:  # Skip invalid positions (same)
                result.append(0)
                continue
            total = 0
            # Iterate over possible placements of zeroes
            for mask in range(q ** n):
                if (mask // (q ** pos1)) % q == 0 and (mask // (q ** pos2)) % q == 0:
                    total += dp(0, mask, 0)
            result.append(total)

    return result

# Test the function
print(count_valid_grid_configurations(2, 2))
