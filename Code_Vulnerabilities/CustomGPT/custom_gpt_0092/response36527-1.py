
def is_valid(grid, r, c, n):
    # Check neighbors: left, right, top, bottom
    neighbors = []
    if c > 0: neighbors.append(grid[r][c - 1])
    if c < n - 1: neighbors.append(grid[r][c + 1])
    if r > 0: neighbors.append(grid[r - 1][c])
    if r < n - 1: neighbors.append(grid[r + 1][c])
    return all(grid[r][c] != neighbor for neighbor in neighbors)

def count_configurations(n, q):
    total = 0
    result = []

    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2: 
                result.append(0)  # Same positions cannot be both zero
                continue

            count = 0
            # Backtracking utility function
            def backtrack(grid, count_zero):
                nonlocal count
                if count_zero == 2:  # We placed both zeros
                    count += 1
                    return
                for r in range(n):
                    for c in range(n):
                        if grid[r][c] == -1:  # Empty cell
                            for value in range(q):
                                grid[r][c] = value
                                if is_valid(grid, r, c, n):
                                    if count_zero < 2 and (r, c) in [(i // n, i % n) for i in [pos1, pos2]]:
                                        backtrack(grid, count_zero + 1)
                                    else:
                                        backtrack(grid, count_zero)
                                grid[r][c] = -1  # Reset for next value
                            return  # Stop after filling first empty cell

            initial_grid = [[-1] * n for _ in range(n)]
            backtrack(initial_grid, 0)
            result.append(count)

    return result

# Example usage
print(count_configurations(2, 2))
