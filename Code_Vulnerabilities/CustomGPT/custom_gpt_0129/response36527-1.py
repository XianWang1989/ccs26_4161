
def count_valid_configurations(n, q, fixed_positions):
    # Create a DP table: dp[mask][r] where mask represents current row state and r is the current row index
    dp = [[0] * (n + 1) for _ in range(1 << n)]
    dp[0][0] = 1  # base case: one way to fill an empty grid

    for r in range(n):  # iterate over rows
        for mask in range(1 << n):  # bitmask for current row's assignments
            if dp[mask][r] == 0:
                continue

            for new_mask in range(1 << n):  # new states for the next row
                if valid_next_row(mask, new_mask, n, fixed_positions[r]):
                    dp[new_mask][r + 1] += dp[mask][r]

    result = []
    for i in range(n):
        for j in range(n):
            total = 0
            for mask in range(1 << n):
                total += dp[mask][n]  # total valid configurations in the last row that met the conditions
            result.append(total)

    return result

def valid_next_row(mask, new_mask, n, fixed):
    # Check if new_mask is valid according to neighbor constraints and fixed positions
    for i in range(n):
        # Check for neighbor constraints
        if (new_mask & (1 << i)) and (i > 0 and (new_mask & (1 << (i - 1)))):  # left neighbor
            return False
        if (new_mask & (1 << i)) and (i < n - 1 and (new_mask & (1 << (i + 1)))):  # right neighbor
            return False

        # Check for fixed positions
        if (fixed[i] != -1) and (new_mask & (1 << i) != fixed[i]):
            return False
    return True

def main(n, q):
    # Example fixed positions
    fixed_positions = [[-1] * n for _ in range(n)]
    fixed_positions[1][1] = 0  # Example fixed position 0 at (1,1)

    return count_valid_configurations(n, q, fixed_positions)

# Example usage
print(main(2, 2))
