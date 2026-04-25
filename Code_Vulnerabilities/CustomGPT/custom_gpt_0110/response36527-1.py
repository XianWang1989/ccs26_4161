
def count_colorings(n, q):
    # Create a memoization table
    memo = {}

    def dfs(row, col, grid, zeros):
        if row == n:
            return 1 if zeros == 2 else 0  # Valid if exactly two zeros are placed

        if (row, col, tuple(map(tuple, grid)), zeros) in memo:
            return memo[(row, col, tuple(map(tuple, grid)), zeros)]

        total = 0
        next_row, next_col = (row, col + 1) if col + 1 < n else (row + 1, 0)

        for num in range(q):
            # Check validity
            if (col > 0 and grid[row][col - 1] == num) or (row > 0 and grid[row - 1][col] == num):
                continue

            grid[row][col] = num

            # Count the zeros
            new_zeros = zeros + (1 if num == 0 else 0)
            total += dfs(next_row, next_col, grid, new_zeros)

        grid[row][col] = -1  # Reset state for backtracking
        memo[(row, col, tuple(map(tuple, grid)), zeros)] = total
        return total

    # Initialize grid and start DFS
    grid = [[-1] * n for _ in range(n)]
    return dfs(0, 0, grid, 0)

def count(n, q):
    results = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 != pos2:
                valid_setups = count_colorings(n, q)
                results.append(valid_setups)
            else:
                results.append(0)  # Same position can't have two zeros

    return results

# Example usage
print(count(2, 2))
