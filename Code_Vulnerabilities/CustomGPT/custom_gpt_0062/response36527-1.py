
def is_valid(grid, n, row, col, value):
    # Check neighboring cells
    if row > 0 and grid[row - 1][col] == value:  # Above
        return False
    if row < n - 1 and grid[row + 1][col] == value:  # Below
        return False
    if col > 0 and grid[row][col - 1] == value:  # Left
        return False
    if col < n - 1 and grid[row][col + 1] == value:  # Right
        return False
    return True

def count_ways(grid, n, q, pos1, pos2, cells_filled, memo):
    if cells_filled == n * n:
        # All cells filled, check conditions
        return 1 if grid[pos1 // n][pos1 % n] == 0 and grid[pos2 // n][pos2 % n] == 0 else 0

    # Convert grid state to tuple for memoization
    state = (tuple(tuple(row) for row in grid), cells_filled)

    if state in memo:
        return memo[state]

    total_ways = 0
    next_pos = cells_filled  # Next position to fill

    for value in range(q):
        row, col = divmod(next_pos, n)
        if is_valid(grid, n, row, col, value):
            grid[row][col] = value
            total_ways += count_ways(grid, n, q, pos1, pos2, cells_filled + 1, memo)
            grid[row][col] = -1  # Backtrack

    memo[state] = total_ways
    return total_ways

def count(n, q):
    result = []
    for pos1 in range(n ** 2):
        for pos2 in range(n ** 2):
            if pos1 == pos2:
                result.append(0)  # Same positions cannot be both 0
                continue

            grid = [[-1 for _ in range(n)] for _ in range(n)]  # Initialize grid with -1
            grid[pos1 // n][pos1 % n] = 0  # Set first position to 0
            grid[pos2 // n][pos2 % n] = 0  # Set second position to 0

            memo = {}
            total = count_ways(grid, n, q, pos1, pos2, 2, memo)  # Start with 2 cells filled
            result.append(total)

    return result

# Example usage
print(count(2, 2))  # Output should be [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
