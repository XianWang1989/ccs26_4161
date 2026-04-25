
def count_configurations(n, q):
    # Precompute valid configurations for one row
    valid_rows = []

    def is_valid(row):
        return all(row[i] != row[i + 1] for i in range(len(row) - 1))

    def generate_rows(curr_row):
        if len(curr_row) == n:
            valid_rows.append(tuple(curr_row))
            return
        for value in range(q):
            curr_row.append(value)
            generate_rows(curr_row)
            curr_row.pop()

    generate_rows([])

    def is_valid_grid(grid):
        for r in range(n):
            for c in range(n):
                if r > 0 and grid[r][c] == grid[r - 1][c]:
                    return False
                if c > 0 and grid[r][c] == grid[r][c - 1]:
                    return False
        return True

    result = []
    for (i, j) in itertools.product(range(n * n), repeat=2):
        total = 0
        for row1 in valid_rows:
            for row2 in valid_rows:
                grid = [row1, row2] + [(0,) * n for _ in range(n - 2)]
                grid[i // n][i % n] = 0
                grid[j // n][j % n] = 0
                if is_valid_grid(grid):
                    total += 1
        result.append(total)
    return result

# Example Usage
print(count_configurations(2, 2))  # Should match the expected output
