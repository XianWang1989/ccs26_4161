
def is_valid_assignment(grid, n, r, c, value):
    # Check the left and upper neighbors
    if c > 0 and grid[r][c - 1] == value:
        return False
    if r > 0 and grid[r - 1][c] == value:
        return False
    return True

def count_ways(n, q, grid, positions, idx):
    if idx == len(positions):
        # All positions are filled, validate and count
        return 1

    count = 0
    r, c = positions[idx]

    for value in range(q):
        if is_valid_assignment(grid, n, r, c, value):
            grid[r][c] = value
            count += count_ways(n, q, grid, positions, idx + 1)
            grid[r][c] = -1  # Reset the position

    return count

def count(n, q):
    result = []
    positions = [(i // n, i % n) for i in range(n * n)]

    for pos1 in positions:
        for pos2 in positions:
            if pos1 == pos2:
                continue
            grid = [[-1] * n for _ in range(n)]  # Initialize grid
            grid[pos1[0]][pos1[1]] = 0  # Set first fixed position
            grid[pos2[0]][pos2[1]] = 0  # Set second fixed position

            # Count configurations for the rest of the grid
            total = count_ways(n, q, grid, positions, 0)
            result.append(total)

    return result

# Example usage
print(count(2, 2))  # Output: Example test case
