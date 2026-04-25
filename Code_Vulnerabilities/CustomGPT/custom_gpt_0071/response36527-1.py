
def is_valid(pos1, pos2, grid, n):
    # Check the constraints for adjacent cells
    for r in range(n):
        for c in range(n):
            if (r, c) == pos1 or (r, c) == pos2:
                continue
            if grid[r][c] == -1:
                continue

            # Check neighbors
            if r > 0 and grid[r][c] == grid[r-1][c]:
                return False
            if r < n-1 and grid[r][c] == grid[r+1][c]:
                return False
            if c > 0 and grid[r][c] == grid[r][c-1]:
                return False
            if c < n-1 and grid[r][c] == grid[r][c+1]:
                return False

    return True

def count_ways(n, q, pos1, pos2):
    def backtrack(grid, idx):
        if idx == n * n:
            return 1 if is_valid(pos1, pos2, grid, n) else 0

        r, c = divmod(idx, n)
        count = 0

        for value in range(q):
            grid[r][c] = value
            count += backtrack(grid, idx + 1)
            grid[r][c] = -1  # Reset cell

        return count

    grid = [[-1 for _ in range(n)] for _ in range(n)]
    return backtrack(grid, 0)

def main_count(n, q):
    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:
                result.append(0)
                continue
            total = count_ways(n, q, divmod(pos1, n), divmod(pos2, n))
            result.append(total)
    return result

assert main_count(2, 2) == [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
