
def is_valid_assignment(lower_row, current_row, q):
    """Check if the current row assignment is valid with respect to the lower row."""
    for col in range(len(current_row)):
        if col > 0 and current_row[col] == current_row[col - 1]:  # Check left neighbor
            return False
        if lower_row[col] == current_row[col]:  # Check top neighbor
            return False
    return True

def count(n, q):
    from itertools import product

    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            total = 0

            # Generate all possible assignments for the grid
            for grid in product(range(q), repeat=n * n):
                if grid[pos1] == 0 and grid[pos2] == 0:
                    valid = True
                    grid_2d = [grid[i * n:(i + 1) * n] for i in range(n)]

                    for row in range(n):
                        if row > 0 and not is_valid_assignment(grid_2d[row - 1], grid_2d[row], q):
                            valid = False
                            break

                    if valid:
                        total += 1

            result.append(total)

    return result

# Example usage
print(count(2, 2))  # Should output the result for n=2 and q=2
