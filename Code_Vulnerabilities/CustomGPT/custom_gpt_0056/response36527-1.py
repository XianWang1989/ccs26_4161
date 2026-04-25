
def count_configurations(n, k, row_mask, col_mask, row, col, dp):
    # If we have filled all rows, return 1 (valid configuration found)
    if row == n:
        return 1

    # Use memoization to avoid redundant calculations
    if (row, col, row_mask, col_mask) in dp:
        return dp[(row, col, row_mask, col_mask)]

    total = 0
    for num in range(k):
        # Check if the number can be placed
        if (row_mask & (1 << num)) == 0 and (col_mask & (1 << num)) == 0:
            # Place count and recurse
            next_row_mask = row_mask | (1 << num)
            next_col_mask = col_mask

            if col == n - 1:
                next_row = row + 1
                next_col = 0
                next_col_mask = 0  # Reset column mask at the end of a row
            else:
                next_row = row
                next_col = col + 1

            total += count_configurations(n, k, next_row_mask, next_col_mask, next_row, next_col, dp)

    dp[(row, col, row_mask, col_mask)] = total
    return total

def count(n, q):
    result = []
    dp = {}

    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:
                result.append(0)  # Can't place at same position
                continue

            # Calculate the number of configurations with positions pos1 and pos2 fixed at 0
            row1, col1 = divmod(pos1, n)
            row2, col2 = divmod(pos2, n)

            total_count = count_configurations(n, q, 0, 0, 0, 0, dp)
            result.append(total_count)

    return result

# Example usage
print(count(2, 2))  # Should output: [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
