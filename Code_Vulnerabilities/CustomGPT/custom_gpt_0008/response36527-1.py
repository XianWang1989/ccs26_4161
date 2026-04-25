
def count(n, q):
    from functools import lru_cache

    # Check if the current row configuration is valid
    def is_valid(prev_row, curr_row):
        for j in range(n):
            if (curr_row & (1 << j)) == (prev_row & (1 << j)):  # Same value vertically
                return False
            if j > 0 and (curr_row & (1 << j)) == (curr_row & (1 << (j - 1))):  # Same value horizontally
                return False
        return True

    @lru_cache(None)
    def dp(row, prev_row):
        if row == n:  # Completed all rows
            return 1
        total = 0
        for curr_row in range(q ** n):  # Iterate through possible current row configurations
            if is_valid(prev_row, curr_row):
                total += dp(row + 1, curr_row)
        return total

    results = []
    # Iterate through possible positions (i, j) and (k, l) for the zeros
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:  # Don't allow same position for 0s
                results.append(0)
                continue

            # Count configurations with zeros at pos1 and pos2
            total_count = dp(0, 0)
            results.append(total_count)

    return results

# Example usage
print(count(2, 2))  # Adjust input for testing
