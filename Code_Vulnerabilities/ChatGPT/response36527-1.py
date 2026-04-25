
def is_valid_row(row, prev_row):
    """ Check if a row is valid compared to the previous row. """
    for c in range(len(row)):
        if c > 0 and row[c] == row[c - 1]:
            return False
        if prev_row is not None and row[c] == prev_row[c]:
            return False
    return True

def count_valid(grid_size, num_colors):
    def dp(row, prev_row):
        if row == grid_size:
            return 1

        total_ways = 0
        for color in range(num_colors):
            new_row = [color if i == 0 else -1 for i in range(grid_size)]
            if is_valid_row(new_row, prev_row):
                # Create a new row varying other column values
                for col in range(1, grid_size):
                    for val in range(num_colors):
                        new_row[col] = val
                        if is_valid_row(new_row, prev_row):
                            total_ways += dp(row + 1, new_row)

        return total_ways

    total = 0
    for pos1 in range(grid_size * grid_size):
        for pos2 in range(grid_size * grid_size):
            if pos1 != pos2:
                grid = [[-1] * grid_size for _ in range(grid_size)]
                grid[pos1 // grid_size][pos1 % grid_size] = 0
                grid[pos2 // grid_size][pos2 % grid_size] = 0
                total += dp(0, [None]*grid_size)

    return total

def count(n, q):
    result = []

    for i in range(n * n):
        for j in range(i + 1, n * n):
            total_ways = count_valid(n, q)
            result.append(total_ways)

    return result

# Example usage
print(count(2, 2))  # Replace this with desired values for n and q
