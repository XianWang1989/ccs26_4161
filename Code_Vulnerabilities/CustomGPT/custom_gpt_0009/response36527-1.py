
def isvalid(pos, grid, n):
    row, col = pos
    # Check the values of the neighboring cells
    for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nrow, ncol = row + drow, col + dcol
        if 0 <= nrow < n and 0 <= ncol < n:
            if grid[nrow][ncol] == grid[row][col]:  # Check for the same value
                return False
    return True

def backtrack(pos, grid, n, q, count, results):
    if pos == n * n:  # We've filled the grid
        results.append(count[0])
        return

    row, col = divmod(pos, n)
    for num in range(q):
        grid[row][col] = num
        if isvalid((row, col), grid, n):
            count[0] += 1  # Increment valid assignment count
            backtrack(pos + 1, grid, n, q, count, results)
            count[0] -= 1  # Decrement to backtrack
        grid[row][col] = -1  # Reset the position

def count(n, q):
    results = []
    initial_grid = [[-1] * n for _ in range(n)]  # Creating an empty grid
    count = [0]  # Use list for mutable integer
    backtrack(0, initial_grid, n, q, count, results)
    return results

# Example usage
print(count(2, 2))  # Output for the grid size 2x2 and 2 colors
