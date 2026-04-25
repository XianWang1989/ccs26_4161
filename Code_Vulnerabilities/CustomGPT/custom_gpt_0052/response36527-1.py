
def is_valid(current_grid, n, row, col, value):
    # Check adjacent neighbors for the value
    if row > 0 and current_grid[row - 1][col] == value:
        return False
    if row < n - 1 and current_grid[row + 1][col] == value:
        return False
    if col > 0 and current_grid[row][col - 1] == value:
        return False
    if col < n - 1 and current_grid[row][col + 1] == value:
        return False
    return True

def count_valid_grids(n, q, i, j):
    from itertools import product

    total_count = 0
    # Generate all possible grid configurations
    for grid in product(range(q), repeat=n*n):
        # Reshape the flat grid into a 2D grid
        current_grid = [list(grid[k:k+n]) for k in range(0, len(grid), n)]
        if (current_grid[i][j] == 0 and 
                is_valid(current_grid, n, i, j, 0)):
            total_count += 1

    return total_count

def count(n, q):
    result = []
    # Iterate through each combination of positions (i, j)
    for i in range(n):
        for j in range(n):
            total = 0
            for k in range(n):
                for l in range(n):
                    if (i, j) != (k, l):  # Ensure distinct positions
                        total += count_valid_grids(n, q, i, j) * count_valid_grids(n, q, k, l)
            result.append(total)
    return result

# Example usage
print(count(2, 2))  # Example output for a 2x2 grid and 2 colors
