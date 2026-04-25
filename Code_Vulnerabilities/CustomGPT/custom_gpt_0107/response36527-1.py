
def is_valid(grid, n, pos):
    # Check the neighbors of the current grid position
    r, c = pos
    value = grid[r][c]
    neighbors = []
    if r > 0: neighbors.append(grid[r-1][c])  # above
    if r < n - 1: neighbors.append(grid[r+1][c])  # below
    if c > 0: neighbors.append(grid[r][c-1])  # left
    if c < n - 1: neighbors.append(grid[r][c+1])  # right
    return all(value != neighbor for neighbor in neighbors)

def count_configurations(n, q, first_zero, second_zero):
    grid = [[-1] * n for _ in range(n)]  # -1 means unassigned
    grid[first_zero[0]][first_zero[1]] = 0
    grid[second_zero[0]][second_zero[1]] = 0

    def dp(pos):
        if pos == n * n:
            return 1  # Valid configuration found
        r, c = divmod(pos, n)

        if grid[r][c] != -1:
            return dp(pos + 1)

        total = 0
        for value in range(1, q):
            grid[r][c] = value
            if is_valid(grid, n, (r, c)):
                total += dp(pos + 1)
            grid[r][c] = -1  # Reset

        return total

    return dp(0)

def count(n, q):
    results = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:
                results.append(0)
                continue
            first_zero = divmod(pos1, n)
            second_zero = divmod(pos2, n)
            results.append(count_configurations(n, q, first_zero, second_zero))

    return results

# Example usage
assert count(2, 2) == [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
