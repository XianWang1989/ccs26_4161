
def is_valid(grid, row, col, value):
    # Check the above position
    if row > 0 and grid[row - 1][col] == value:
        return False
    # Check the below position
    if row < len(grid) - 1 and grid[row + 1][col] == value:
        return False
    # Check the left position
    if col > 0 and grid[row][col - 1] == value:
        return False
    # Check the right position
    if col < len(grid) - 1 and grid[row][col + 1] == value:
        return False
    return True

def assign_values(grid, n, q, index, zero_positions, results):
    if index == n * n:
        # When we fill the grid, check our zero positions constraints.
        if grid[zero_positions[0]] == 0 and grid[zero_positions[1]] == 0:
            results[0] += 1
        return

    row = index // n
    col = index % n

    for value in range(q):
        if is_valid(grid, row, col, value):
            grid[index] = value
            assign_values(grid, n, q, index + 1, zero_positions, results)
            grid[index] = -1  # Reset for backtracking

def count_ways(n, q):
    # Initialize grid with -1 (unassigned)
    grid = [-1] * (n * n)
    results = [0]  # Using a list to hold the count as mutable
    # Consider every pair of zero positions
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 != pos2:
                grid[pos1] = 0
                grid[pos2] = 0
                assign_values(grid, n, q, 0, (pos1, pos2), results)
                grid[pos1] = -1  # Reset
                grid[pos2] = -1  # Reset
    return results[0]

# Test the function
print(count_ways(2, 2))  # Example usage
