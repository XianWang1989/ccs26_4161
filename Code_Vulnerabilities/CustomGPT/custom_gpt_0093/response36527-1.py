
def count_ways(n, q):
    from functools import lru_cache

    # Precompute the valid neighbors for each color
    valid_neighbors = [[set() for _ in range(q)] for _ in range(q)]
    for i in range(q):
        for j in range(q):
            if i != j:
                valid_neighbors[i].add(j)

    @lru_cache(None)
    def dp(row, col, mask):
        # If we are out of bounds, continue
        if row == n:
            return 1 if mask == 0 else 0

        # If we reach the end of the row, go to the next row
        if col == n:
            return dp(row + 1, 0, mask)

        # Count valid assignments for grid[row][col]
        total_ways = 0

        for color in range(q):
            # Check if the color is valid based on the mask and neighbors
            if (mask & (1 << color)) == 0:
                # Check neighbors
                if (col > 0 and grid[row][col - 1] == color) or (row > 0 and grid[row - 1][col] == color):
                    continue

                # Set color
                prev = grid[row][col]
                grid[row][col] = color
                total_ways += dp(row, col + 1, mask | (1 << color))
                # Reset color
                grid[row][col] = prev

        return total_ways

    results = []

    for pos1 in range(n * n):
        for pos2 in range(n * n):
            # Initialize grid with -1s
            global grid
            grid = [[-1] * n for _ in range(n)]
            grid[pos1 // n][pos1 % n] = 0  # Set the first fixed position to 0
            grid[pos2 // n][pos2 % n] = 0  # Set the second fixed position to 0

            # Count the ways to fill the grid
            count = dp(0, 0, 0)
            results.append(count)

    return results

# Example usage
print(count_ways(2, 2))  # Example call for n=2, q=2
