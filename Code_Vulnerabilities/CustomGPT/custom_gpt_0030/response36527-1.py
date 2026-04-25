
def count_valid_assignments(n, q):
    def is_valid(grid, row, col, value):
        # Check the left, right, top, and bottom neighbors
        if col > 0 and grid[row][col - 1] == value:
            return False
        if col < n - 1 and grid[row][col + 1] == value:
            return False
        if row > 0 and grid[row - 1][col] == value:
            return False
        if row < n - 1 and grid[row + 1][col] == value:
            return False
        return True

    def backtrack(grid, assignments, zero_positions):
        if assignments == n * n:
            count = 1
            for (i, j) in zero_positions:
                grid[i][j] = 0  # Ensure zeros at specified positions
            return count
        count = 0
        row = assignments // n
        col = assignments % n

        for value in range(q):
            if is_valid(grid, row, col, value):
                grid[row][col] = value
                count += backtrack(grid, assignments + 1, zero_positions)
                grid[row][col] = -1  # Reset for backtracking
        return count

    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:
                result.append(0)  # Same position not allowed
                continue

            # Assign zero positions based on index
            zero_positions = [(pos1 // n, pos1 % n), (pos2 // n, pos2 % n)]
            grid = [[-1] * n for _ in range(n)]  # Initialize grid with -1
            total_count = backtrack(grid, 0, zero_positions)
            result.append(total_count)

    return result

# Example usage
print(count_valid_assignments(2, 2))
