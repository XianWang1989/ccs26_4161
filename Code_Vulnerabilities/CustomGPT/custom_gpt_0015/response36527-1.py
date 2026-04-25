
def count_ways(n, q):
    def is_valid(r, c, value):
        if r > 0 and grid[r-1][c] == value:  # check top
            return False
        if c > 0 and grid[r][c-1] == value:  # check left
            return False
        return True

    def backtrack(pos, count):
        if pos == n * n:
            return 1 if count == positions.count(0) else 0

        r, c = divmod(pos, n)
        total = 0

        if (r, c) in positions:
            # For given (i, j) and (k, l) positions which must be 0
            total += backtrack(pos + 1, count)
        else:
            for v in range(q):
                if is_valid(r, c, v):
                    grid[r][c] = v
                    total += backtrack(pos + 1, count)
                    grid[r][c] = -1  # Reset for backtrack

        return total

    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 != pos2:
                grid = [[-1] * n for _ in range(n)]
                positions = [pos1, pos2]  # The positions that must be zero
                grid[divmod(pos1, n)[0]][divmod(pos1, n)[1]] = 0
                grid[divmod(pos2, n)[0]][divmod(pos2, n)[1]] = 0
                result.append(backtrack(0, positions.count(0)))

    return result

# Example usage:
print(count_ways(2, 2))  # Output for n=2, q=2
