
def is_valid(grid, n, row, col, val):
    # Check if placing val at (row, col) is valid
    for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
        nrow, ncol = row + drow, col + dcol
        if 0 <= nrow < n and 0 <= ncol < n and grid[nrow][ncol] == val:
            return False
    return True

def count_valid_ways(n, q, fixed_positions):
    results = []

    # Dynamic programming table
    dp = [[0] * (1 << (n * n)) for _ in range(n * n)]

    # Initialize dp for single empty grid placements
    for mask in range(1 << (n * n)):
        dp[0][mask] = 1  # Base case

    # Iterate over each cell
    for cell in range(n * n):
        row, col = divmod(cell, n)
        for mask in range(1 << (n * n)):
            # Count configurations for each current mask state
            if dp[cell][mask] > 0:
                for color in range(q):
                    new_mask = mask
                    # Check if this color can be placed
                    if is_valid(mask, n, row, col, color):
                        new_mask |= (1 << cell)  # Place color in the mask
                        dp[cell + 1][new_mask] += dp[cell][mask]

    # Count valid placements for each fixed position
    for pos1 in range(len(fixed_positions)):
        for pos2 in range(pos1 + 1, len(fixed_positions)):
            count = 0
            for mask in range(1 << (n * n)):
                if (mask & (1 << fixed_positions[pos1])) == 0 and (mask & (1 << fixed_positions[pos2])) == 0:
                    count += dp[n * n][mask]
            results.append(count)

    return results

def count(n, q):
    # Generate all fixed positions in a flat manner
    fixed_positions = [(i, j) for i in range(n) for j in range(n)]
    results = []

    for (i, j) in fixed_positions:
        for (k, l) in fixed_positions:
            if (i, j) != (k, l):
                index1 = i * n + j
                index2 = k * n + l
                result = count_valid_ways(n, q, (index1, index2))
                results.append(result)

    return results

# Sample Test
print(count(2, 2))  # Example output
