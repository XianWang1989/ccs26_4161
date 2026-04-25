
def is_valid(grid, n, r, c, value):
    # Check horizontally and vertically adjacent cells
    if r > 0 and grid[r - 1][c] == value:
        return False
    if r < n - 1 and grid[r + 1][c] == value:
        return False
    if c > 0 and grid[r][c - 1] == value:
        return False
    if c < n - 1 and grid[r][c + 1] == value:
        return False
    return True

def count_configurations(n, q, grid, positions, index):
    if index == len(positions):
        return 1  # Valid configuration found

    count = 0
    r, c = positions[index]

    for value in range(q):
        if is_valid(grid, n, r, c, value):
            grid[r][c] = value  # Assign value
            count += count_configurations(n, q, grid, positions, index + 1)
            grid[r][c] = -1  # Backtrack

    return count

def count(n, q):
    positions = [(i, j) for i in range(n) for j in range(n)]
    grid = [[-1] * n for _ in range(n)]  # Initialize grid
    result = []

    for pos1 in positions:
        for pos2 in positions:
            if pos1 != pos2:  # Ensure different positions
                grid[pos1[0]][pos1[1]] = 0  # Assign 0 to first position
                grid[pos2[0]][pos2[1]] = 0  # Assign 0 to second position
                count_valid = count_configurations(n, q, grid, positions, 0)
                result.append(count_valid)
                grid[pos1[0]][pos1[1]] = -1  # Reset
                grid[pos2[0]][pos2[1]] = -1  # Reset

    return result

# Example usage:
print(count(2, 2))  # Call the function for n=2, q=2
