
def is_valid(grid, n, row, col, value):
    for dr in [-1, 1]:
        if 0 <= row + dr < n and grid[row + dr][col] == value:
            return False
    for dc in [-1, 1]:
        if 0 <= col + dc < n and grid[row][col + dc] == value:
            return False
    return True

def backtrack(grid, n, q, idx, count, positions):
    if idx == n * n:
        count[0] += 1
        return

    row, col = divmod(idx, n)
    for value in range(q):
        if (row, col) in positions and value != 0:
            continue  # Skip if this position must be 0
        if is_valid(grid, n, row, col, value):
            grid[row][col] = value
            backtrack(grid, n, q, idx + 1, count, positions)
            grid[row][col] = -1  # Backtrack

def count(n, q):
    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            if pos1 == pos2:
                result.append(0)
                continue

            grid = [[-1] * n for _ in range(n)]
            count = [0]
            positions = {(pos1 // n, pos1 % n), (pos2 // n, pos2 % n)}
            grid[pos1 // n][pos1 % n] = 0
            grid[pos2 // n][pos2 % n] = 0

            backtrack(grid, n, q, 0, count, positions)
            result.append(count[0])

    return result

# Example usage
print(count(2, 2))  # Expected output based on problem description
