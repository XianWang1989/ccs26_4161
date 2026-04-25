
def count_valid_configurations(n, q):
    from itertools import product

    def is_valid(grid, n, r, c, value):
        # Check neighboring cells
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == value:
                    return False
        return True

    def backtrack(grid, empty_positions, idx):
        if idx == len(empty_positions):
            # Check for a valid configuration
            for (i, j), (k, l) in empty_positions:
                if grid[i][j] == 0 and grid[k][l] == 0:
                    return 1
            return 0

        total_count = 0
        (r, c) = empty_positions[idx]
        for value in range(q):
            if is_valid(grid, n, r, c, value):
                grid[r][c] = value
                total_count += backtrack(grid, empty_positions, idx + 1)
                grid[r][c] = -1  # Reset for backtracking

        return total_count

    # Initialize variables
    total_results = []
    empty_positions = [(i, j) for i in range(n) for j in range(n)]

    # Iterate over all pairs of positions (i, j) and (k, l)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if (i, j) != (k, l):
                        grid = [[-1] * n for _ in range(n)]
                        empty_cells = [(i, j), (k, l)]
                        count = backtrack(grid, empty_cells, 0)
                        total_results.append(count)

    return total_results

# Test the function
print(count_valid_configurations(2, 2))  # Example test for n=2, q=2
