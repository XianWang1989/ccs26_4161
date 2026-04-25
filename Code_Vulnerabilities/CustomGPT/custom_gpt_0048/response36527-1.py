
def count_valid_assignments(n, q):
    from functools import lru_cache

    @lru_cache(None)
    def dp(row, prev_row_mask, prev_prev_row_mask):
        if row == n:
            return 1

        total_ways = 0
        for current_mask in range(q ** n):
            if is_valid(current_mask, prev_row_mask, prev_prev_row_mask, q, n):
                total_ways += dp(row + 1, current_mask, prev_row_mask)

        return total_ways

    total_results = []
    for pos1 in range(n ** 2):
        for pos2 in range(pos1 + 1, n ** 2):
            result = dp(0, 0, 0)  # Start with 0 for all rows
            total_results.append(result)

    return total_results

def is_valid(current_mask, prev_row_mask, prev_prev_row_mask, q, n):
    # Check if the current mask follows neighbor rules.
    for i in range(n):
        current_value = (current_mask // (q ** i)) % q
        # Check against the previous row
        if i > 0:
            left_value = (current_mask // (q ** (i - 1))) % q
            if current_value == left_value:
                return False
        # Check against the upper row
        above_value = (prev_row_mask // (q ** i)) % q
        if current_value == above_value:
            return False
        # Edge case for the first row
        if row > 0:
            above_above_value = (prev_prev_row_mask // (q ** i)) % q
            if current_value == above_above_value:
                return False
    return True

# Example usage:
print(count_valid_assignments(2, 2))
