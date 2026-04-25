
def is_valid(position, state, n):
    # Check if the current position can be assigned a value based on neighbors in the grid.
    row, col = position
    for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbor_row, neighbor_col = row + d_row, col + d_col
        if 0 <= neighbor_row < n and 0 <= neighbor_col < n:
            neighbor_index = neighbor_row * n + neighbor_col
            if state[neighbor_index] == state[row * n + col]:
                return False
    return True

def count_valid_assignments(n, q):
    m = n * n
    result = []

    # Iterate over all possible pairs of positions (i,j) and (k,l) to assign values of 0
    for pos1 in range(m):
        for pos2 in range(m):
            if pos1 == pos2:  # Skip if same position
                result.append(0)
                continue

            total = 0

            # Iterate over all possible states of the grid using bitmasking
            for state in range(q ** m):
                # Convert state into a grid-like representation
                grid = [(state // (q ** i)) % q for i in range(m)]

                # Set positions for 0
                grid[pos1] = 0
                grid[pos2] = 0

                # Check if the assignment is valid
                if all(is_valid((r, c), grid, n) for r in range(n) for c in range(n)):
                    total += 1

            result.append(total)

    return result

# Example Usage
print(count_valid_assignments(2, 2))
