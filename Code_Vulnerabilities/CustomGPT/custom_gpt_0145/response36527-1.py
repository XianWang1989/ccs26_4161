
def count_valid_assignments(n, q):
    from functools import lru_cache

    @lru_cache(None)
    def dp(row, mask1, mask2):
        if row == n:  # All rows are assigned
            return 1

        total = 0
        # Generate all possible assignments for this row
        for mask in range(1 << q):
            # Check if this mask is valid given the previous row's mask
            if valid(mask1, mask2, mask, n, q):
                total += dp(row + 1, mask2, mask)  # Move to the next row

        return total

    def valid(mask1, mask2, mask, n, q):
        # Validate against constraints for this row
        for j in range(q):
            if (mask >> j) & 1:  # If we are using value j in this mask
                # Check left neighbor
                if (j == (mask & ((1 << (j + 1)) - 1))) or (j == (mask2 & ((1 << (j + 1)) - 1))):
                    return False
                # Check top neighbor
                if (j == (mask1 & ((1 << (j + 1)) - 1))):
                    return False

        return True

    total_count = dp(0, 0, 0)
    return total_count

# Example usage:
n = 2
q = 2
result = count_valid_assignments(n, q)
print(result)
