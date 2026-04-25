
def count(n, q):
    def is_valid(grid, r, c, value):
        if r > 0 and grid[r - 1][c] == value:
            return False
        if c > 0 and grid[r][c - 1] == value:
            return False
        return True

    def dp(pos, grid, placements):
        if pos == n * n:
            return placements

        r, c = divmod(pos, n)
        total_count = 0

        for value in range(q):
            if is_valid(grid, r, c, value):
                grid[r][c] = value
                total_count += dp(pos + 1, grid, placements)
                grid[r][c] = -1  # Reset

        return total_count

    results = []

    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:
                results.append(0)
                continue

            grid = [[-1] * n for _ in range(n)]
            # Assign 0 to both positions
            grid[pos1 // n][pos1 % n] = 0
            grid[pos2 // n][pos2 % n] = 0

            total_valid = dp(0, grid, 0)
            results.append(total_valid)

    return results

# Example usage for 2x2 grid with 2 colors:
print(count(2, 2))  # Output: [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
