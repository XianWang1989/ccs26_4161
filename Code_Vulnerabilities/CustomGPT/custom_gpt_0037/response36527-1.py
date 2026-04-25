
def count_colorings(n, q):
    from functools import lru_cache

    @lru_cache(None)
    def dp(row, prev_mask):
        if row == n:
            return 1

        total = 0
        for mask in range(1 << (n * q)):
            # Ensure no adjacent cells in the same row share colors
            valid = True
            for col in range(n):
                if (prev_mask >> (col * q)) & 1:
                    continue
                for color in range(q):
                    if (mask & (1 << (col * q + color))) and (prev_mask & (1 << (col * q + color))):
                        valid = False
                        break

            if valid:
                total += dp(row + 1, mask)

        return total

    # Prepare masks for each row
    result = []
    for i in range(n * n):
        result.append(dp(0, 0))

    return result

def count(n, q):
    return count_colorings(n, q)

# Example usage
result = count(2, 2)
print(result)  # Example output for n=2, q=2
