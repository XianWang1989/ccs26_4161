
def count(arr, pos1, pos2, n, q):
    # Dynamic programming memoization
    memo = {}

    def dp(mask, row):
        # If we filled the last row
        if row == n:
            return 1

        # Use the memoization dictionary to avoid recalculating
        if (mask, row) in memo:
            return memo[(mask, row)]

        total = 0
        for color in range(q):
            # Check if this color can be used in this position
            if (mask & (1 << color)) == 0:
                # Proceed to the next row applying this color
                next_mask = mask | (1 << color)
                total += dp(next_mask, row + 1)

        # Save result in memo
        memo[(mask, row)] = total
        return total

    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            # Only proceed if the two positions are distinct
            if pos1 != pos2:
                # Get the starting state without the two positions assigned
                grid_mask = (1 << arr[pos1]) | (1 << arr[pos2])
                result.append(dp(grid_mask, 0))
            else:
                result.append(0)  # If positions are the same, it's invalid

    return result

def generate_possibilities(n, q):
    z = [0] * (n * n)
    pos_count = []

    for i in range(n * n):
        for v in range(q):
            z[i] = v
            pos_count.append(count(z, (i, 0), (i, 1), n, q))

    return pos_count

# Example usage
print(generate_possibilities(2, 2))  # Adjust n and q as you see fit
