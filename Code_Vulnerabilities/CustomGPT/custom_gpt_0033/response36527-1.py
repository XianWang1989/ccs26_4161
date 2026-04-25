
def is_valid(grid, r, c, value):
    # Check adjacent cells for validity
    if r > 0 and grid[r-1][c] == value: return False  # Up
    if r < len(grid) - 1 and grid[r+1][c] == value: return False  # Down
    if c > 0 and grid[r][c-1] == value: return False  # Left
    if c < len(grid) - 1 and grid[r][c+1] == value: return False  # Right
    return True

def count_ways(n, q, grid, positions, index):
    if index == len(positions):
        # All positions filled, count valid grid configurations
        return 1

    r, c = positions[index]
    total_ways = 0

    for value in range(q):
        if is_valid(grid, r, c, value):
            grid[r][c] = value
            total_ways += count_ways(n, q, grid, positions, index + 1)
            grid[r][c] = -1  # Reset cell

    return total_ways

def count(n, q):
    # Generate all positions to be filled with 0s
    positions = [(i // n, i % n) for i in range(n * n)]
    results = []

    for pos1 in range(n * n):
        for pos2 in range(pos1 + 1, n * n):
            grid = [[-1] * n for _ in range(n)]
            grid[positions[pos1][0]][positions[pos1][1]] = 0
            grid[positions[pos2][0]][positions[pos2][1]] = 0

            total = count_ways(n, q, grid, positions, 0)
            results.append(total)

    return results

# Test the implementation
print(count(2, 2))  # Example output for n=2 and q=2
