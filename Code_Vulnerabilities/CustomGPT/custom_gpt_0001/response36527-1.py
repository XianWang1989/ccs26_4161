
def is_valid(grid, r, c, value):
    # Check the left, right, top, and bottom neighbors
    if r > 0 and grid[r-1][c] == value:
        return False
    if r < len(grid) - 1 and grid[r+1][c] == value:
        return False
    if c > 0 and grid[r][c-1] == value:
        return False
    if c < len(grid) - 1 and grid[r][c+1] == value:
        return False
    return True

def count_assignments(n, q, grid, positions, current_pos):
    if current_pos == n * n:  # All positions are filled
        return 1 if positions.count(0) == 2 else 0

    total_counts = 0
    if current_pos in positions:  # Skip filled positions
        return count_assignments(n, q, grid, positions, current_pos + 1)

    for value in range(q):
        r, c = divmod(current_pos, n)
        if is_valid(grid, r, c, value):
            grid[r][c] = value
            total_counts += count_assignments(n, q, grid, positions, current_pos + 1)
            grid[r][c] = -1  # Reset

    return total_counts

def count(n, q):
    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            if pos1 == pos2:  # Avoid counting the same position
                result.append(0)
                continue

            positions = [pos1, pos2]
            grid = [[-1] * n for _ in range(n)]
            total = count_assignments(n, q, grid, positions, 0)
            result.append(total)

    return result

# Sample usage
n = 2
q = 2
print(count(n, q))  # Example call
