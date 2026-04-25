
def is_valid(grid, n, r, c, color):
    # Check horizontally and vertically adjacent cells
    if r > 0 and grid[r-1][c] == color:
        return False
    if r < n-1 and grid[r+1][c] == color:
        return False
    if c > 0 and grid[r][c-1] == color:
        return False
    if c < n-1 and grid[r][c+1] == color:
        return False
    return True

def count_assignments(n, q):
    def backtrack(pos, count_0_pos1, count_0_pos2):
        if pos == n * n:
            return 1 if count_0_pos1 and count_0_pos2 else 0

        r, c = pos // n, pos % n
        total = 0

        for color in range(q):
            if is_valid(grid, n, r, c, color):
                grid[r][c] = color

                if (r, c) in [(i, j), (k, l)] and color == 0:
                    if (r, c) == (i, j):
                        count_0_pos1 += 1
                    if (r, c) == (k, l):
                        count_0_pos2 += 1

                total += backtrack(pos + 1, count_0_pos1, count_0_pos2)
                grid[r][c] = -1  # Reset

        return total

    grid = [[-1] * n for _ in range(n)]
    results = []

    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:
                results.append(0)
                continue
            i, j = divmod(pos1, n)
            k, l = divmod(pos2, n)
            total_count = backtrack(0, 0, 0)
            results.append(total_count)

    return results

# Example usage
n = 2
q = 2
print(count_assignments(n, q))
