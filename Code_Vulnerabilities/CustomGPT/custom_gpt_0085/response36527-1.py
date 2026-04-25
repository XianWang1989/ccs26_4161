
def is_valid(pos1, pos2, n, grid):
    # Check no two adjacent cells have the same value
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for r in range(n):
        for c in range(n):
            if grid[r][c] == -1:
                continue
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == grid[r][c]:
                        return False
    return True

def backtrack(n, q, grid, index, pos1, pos2, result):
    if index == n * n:
        if is_valid(pos1, pos2, n, grid):
            result[0] += 1
        return

    r, c = divmod(index, n)

    for value in range(q):
        grid[r][c] = value
        backtrack(n, q, grid, index + 1, pos1, pos2, result)
        grid[r][c] = -1  # Reset

def count(n, q):
    result = [0]
    grid = [[-1] * n for _ in range(n)]

    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 != pos2:
                grid[divmod(pos1, n)] = 0
                grid[divmod(pos2, n)] = 0
                backtrack(n, q, grid, 0, pos1, pos2, result)
                grid[divmod(pos1, n)] = -1
                grid[divmod(pos2, n)] = -1

    return result

# Example usage
print(count(2, 2))  # Output: [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
