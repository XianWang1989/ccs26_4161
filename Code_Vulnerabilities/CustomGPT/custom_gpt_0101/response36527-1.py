
def count_valid_grids(n, q):
    from itertools import product

    def is_valid(grid):
        for r in range(n):
            for c in range(n):
                value = grid[r][c]
                # Check horizontal and vertical neighbors
                if (c > 0 and grid[r][c - 1] == value) or (c < n - 1 and grid[r][c + 1] == value) or \
                   (r > 0 and grid[r - 1][c] == value) or (r < n - 1 and grid[r + 1][c] == value):
                    return False
        return True

    results = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            total = 0
            for values in product(range(q), repeat=n * n):
                grid = [values[i * n:(i + 1) * n] for i in range(n)]
                if values[pos1] == 0 and values[pos2] == 0 and is_valid(grid):
                    total += 1
            results.append(total)

    return results

# Example usage
print(count_valid_grids(2, 2))
