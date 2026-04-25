
def count_valid_assignments(n, q):
    from itertools import product

    # Memoization table
    memo = {}

    def is_valid(grid, row, col, value):
        # Check left, right, top, bottom
        if col > 0 and grid[row][col - 1] == value:
            return False
        if col < n - 1 and grid[row][col + 1] == value:
            return False
        if row > 0 and grid[row - 1][col] == value:
            return False
        if row < n - 1 and grid[row + 1][col] == value:
            return False
        return True

    def dp(position, count):
        if position == n * n:
            return 1 if count == 0 else 0
        if (position, count) in memo:
            return memo[(position, count)]

        row, col = divmod(position, n)
        total_ways = 0

        for value in range(q):
            if count == 0 and value == 0:
                # Place the value at the current position
                grid[row][col] = value
                total_ways += dp(position + 1, count)
                grid[row][col] = -1  # Revert the change
            elif is_valid(grid, row, col, value):
                grid[row][col] = value
                total_ways += dp(position + 1, count - (1 if value == 0 else 0))
                grid[row][col] = -1  # Revert the change

        memo[(position, count)] = total_ways
        return total_ways

    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:
                result.append(0)  # Cannot place two zeros in the same position
                continue

            grid = [[-1] * n for _ in range(n)]  # Initialize grid with -1
            grid[divmod(pos1, n)] = 0
            grid[divmod(pos2, n)] = 0
            memo.clear()  # Clear memoization for each pair
            total = dp(0, 2)  # Start with 2 slots for zero values
            result.append(total)

    return result

# Example Usage
print(count_valid_assignments(2, 2))
