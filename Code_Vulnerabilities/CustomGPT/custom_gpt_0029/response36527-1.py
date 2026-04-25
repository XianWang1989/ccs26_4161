
def count_assignments(n, q):
    from functools import lru_cache

    # Cache the results of the DP function
    @lru_cache(None)
    def dp(row, prev_mask):
        if row == n:
            return 1  # Reached the end of the grid
        count = 0

        # Generate all possible masks for the current row
        for curr_mask in range(1 << q):
            # Check if the current mask is valid
            if is_valid(prev_mask, curr_mask):
                count += dp(row + 1, curr_mask)

        return count

    def is_valid(prev_mask, curr_mask):
        # Check if the current row's mask is valid with the previous row's mask
        for value in range(q):
            if (curr_mask & (1 << value)) > 0 and (prev_mask & (1 << value)) > 0:
                return False  # Same value in adjacent rows
        return True

    result = []
    for i in range(n * n):
        for j in range(i + 1, n * n):
            total_count = 0

            # Iterate over all possible row configurations
            for first_row_mask in range(1 << q):
                if is_fixed_positions(first_row_mask, i, j):
                    total_count += dp(1, first_row_mask)

            result.append(total_count)

    return result

def is_fixed_positions(mask, pos1, pos2):
    # Check the positions of (i, j) if they are included in the mask
    if ((mask >> 0) & 1) and (pos1 == 0 or pos2 == 0):
        return True  # Contains the first fixed position (0)
    return False

# Test
print(count_assignments(2, 2))  # Example usage
