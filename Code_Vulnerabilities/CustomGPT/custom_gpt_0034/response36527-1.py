
def count_valid_grid_assignments(n, q):
    from functools import lru_cache

    # Function to calculate valid assignments
    @lru_cache(None)
    def count(row, prev_mask):
        if row == n:  # All rows are filled
            return 1

        total = 0
        for mask in range(1 << (n * 2)):  # Each row can have up to 2*n states
            if is_valid(mask, prev_mask, n):
                total += count(row + 1, mask)

        return total

    # Check if the current mask is valid with respect to the previous mask
    def is_valid(mask, prev_mask, n):
        # Compare to ensure no two adjacent cells are the same
        current_row = [(mask >> (i * 2)) & 3 for i in range(n)]  # Decode mask

        for i in range(n):
            if current_row[i] == 0:  # Check for value 0
                if prev_mask & (1 << i):  # vertically adjacent
                    return False
            if i > 0 and current_row[i] == current_row[i - 1]:  # horizontally adjacent
                return False

        return True

    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            # Count valid configurations considering pos1 and pos2 are zero
            total = 0
            for mask in range(1 << (n * 2)):  # Each row can have up to 2*n states
                if (mask & (1 << pos1)) == 0 and (mask & (1 << pos2)) == 0:
                    total += count(0, mask)
            result.append(total)

    return result

# Example usage
print(count_valid_grid_assignments(2, 2))
