
def is_valid(new_row, prev_row, n, q):
    for i in range(n):
        if (new_row & (1 << i)) != 0:  # Check if the i-th bit is set
            if (prev_row & (1 << i)) != 0:  # Check if there's a value in the same column in the previous row
                return False
            if i > 0 and (new_row & (1 << (i - 1))) != 0:  # Check left neighbor
                return False
            if i < n - 1 and (new_row & (1 << (i + 1))) != 0:  # Check right neighbor
                return False
    return True

def count(n, q):
    # DP table
    dp = [[0] * (1 << n) for _ in range(n + 1)]

    # Go row by row
    for row in range(1, n + 1):
        for mask in range(1 << n):
            dp[row][mask] = 0
            # Now we need to assign `q` colors, we can fill `mask` with valid colors
            for color in range(q):
                new_row = 0
                for i in range(n):
                    if (mask & (1 << i)) != 0:  # if i-th bit is set
                        new_row |= (color << (i * 2))  # Use 2 bits for each color
                if is_valid(new_row, mask, n, q):
                    dp[row][new_row] += 1

    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            total = sum(dp[n][:])  # Sum all valid configurations
            result.append(total)

    return result

# Example usage
print(count(2, 2))  # Assuming count(2, 2) should return the respective results based on the conditions.
