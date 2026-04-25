
def is_valid_transition(prev_row, curr_row, q):
    for j in range(len(curr_row)):
        if (j > 0 and curr_row[j] == curr_row[j - 1]) or (prev_row[j] == curr_row[j]):
            return False
    return True

def count_valid_grids(n, q):
    all_rows = []

    # Generate all possible rows for the grid
    for i in range(q ** n):
        row = []
        value = i
        for _ in range(n):
            row.append(value % q)
            value //= q
        all_rows.append(row)

    total_count = [[0] * (q ** n) for _ in range(n + 1)]
    total_count[0][0] = 1  # One way to fill zero rows

    for i in range(1, n + 1):
        for prev_row in all_rows:
            for curr_row in all_rows:
                if is_valid_transition(prev_row, curr_row, q):
                    total_count[i][tuple(curr_row)] += total_count[i - 1][tuple(prev_row)]

    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            total = 0
            for row in all_rows:
                if row[pos1 % n] == 0 and row[pos2 % n] == 0:
                    total += total_count[n][tuple(row)]
            result.append(total)

    return result

# Example usage
print(count_valid_grids(2, 2))
