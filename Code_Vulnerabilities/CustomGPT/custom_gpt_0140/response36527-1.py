
def count(n, q):
    from functools import lru_cache

    # Pre-compute valid configurations for a single row with given constraints
    def generate_valid_rows(used_values):
        if len(used_values) > n:
            return []
        # Try all combinations of values for the current row
        valid_rows = []
        for i in range(q):
            if i not in used_values:
                for row in generate_valid_rows(used_values | {i}):
                    valid_rows.append([i] + row)
        if not used_values:
            valid_rows.append([])
        return valid_rows

    # Store valid row configurations
    valid_rows = generate_valid_rows(set())

    # DP to count configurations for the grid
    @lru_cache(None)
    def dp(row, last_row, count_0_positions):
        if row == n:
            return count_0_positions

        total_count = 0
        for r in valid_rows:
            if is_valid_transition(last_row, r):
                total_count += dp(row + 1, tuple(r), count_0_positions)

        return total_count

    # Check if transition to new row is valid
    def is_valid_transition(last_row, new_row):
        for i in range(n):
            if last_row[i] == new_row[i]:  # No horizontal adjacent same values
                return False
            if row > 0 and new_row[i] == grid[row-1][i]:  # No vertical adjacent same values
                return False
        return True

    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            grid = [[0] * n for _ in range(n)]
            grid[pos1 // n][pos1 % n] = grid[pos2 // n][pos2 % n] = 0
            total = dp(0, tuple([None] * n), 1 if pos1 == pos2 else 2)
            result.append(total)

    return result

# Example usage
print(count(2, 2))
