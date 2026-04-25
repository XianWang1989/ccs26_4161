
def is_valid_configuration(row, prev_row, q):
    for j in range(len(row)):
        if row[j] == prev_row[j] or (j > 0 and row[j] == row[j - 1]):
            return False
    return True

def count_valid_configurations(n, q):
    from itertools import product

    # Initialize total counts for each configuration
    total_counts = [[0] * (n * n) for _ in range(n * n)]

    # Generate all possible row configurations
    all_rows = list(product(range(q), repeat=n))

    # Count valid configurations
    for idx1 in range(len(all_rows)):
        for idx2 in range(len(all_rows)):
            if is_valid_configuration(all_rows[idx1], all_rows[idx2], q):
                for pos1 in range(n**2):
                    for pos2 in range(n**2):
                        if pos1 // n == idx1 and pos2 // n == idx2:
                            total_counts[pos1][pos2] += 1

    return total_counts

# Example usage
n = 2
q = 2
result = count_valid_configurations(n, q)

# print the result for demonstration
for row in result:
    print(row)
