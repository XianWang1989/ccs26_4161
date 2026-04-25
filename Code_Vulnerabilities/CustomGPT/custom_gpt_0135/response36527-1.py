
def is_valid(state, row, col, n):
    if row > 0:  # Check the cell above
        if state[row - 1][col] == state[row][col]:
            return False
    if col > 0:  # Check the cell to the left
        if state[row][col - 1] == state[row][col]:
            return False
    return True

def count_configurations(n, q, fixed_positions):
    total_count = 0

    # Function to backtrack through the grid
    def backtrack(row, col, state):
        nonlocal total_count
        if row == n:  # We've reached past the last row
            total_count += 1
            return

        next_row, next_col = (row, col + 1) if col + 1 < n else (row + 1, 0)

        for value in range(q):
            state[row][col] = value
            if is_valid(state, row, col, n):
                backtrack(next_row, next_col, state)

    # Initialize an empty state
    state = [[-1] * n for _ in range(n)]

    # Apply fixed positions
    for pos in fixed_positions:
        state[pos[0]][pos[1]] = 0

    backtrack(0, 0, state)
    return total_count

def count(n, q):
    result = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if (i, j) != (k, l):  # Ensure unique positions
                        fixed_positions = [(i, j), (k, l)]
                        total = count_configurations(n, q, fixed_positions)
                        result.append(total)

    return result

# Example usage
print(count(2, 2))  # Expected output example for n=2, q=2
