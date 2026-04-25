
def count_ways(n, q):
    # Precompute valid configurations
    valid = []

    for mask in range(q ** n):
        grid = [mask // (q ** i) % q for i in range(n)]

        valid_mask = True
        for i in range(n):
            for j in range(n):
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    valid_mask = False
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    valid_mask = False
        if valid_mask:
            valid.append(grid)

    results = []

    for pos1 in range(n * n):
        for pos2 in range(n * n):
            total = 0
            for grid in valid:
                if grid[pos1] == 0 and grid[pos2] == 0:
                    total += 1
            results.append(total)

    return results

# Example usage:
print(count_ways(2, 2))
