
def count_valid_assignments(n, q):
    from itertools import product

    # Precompute neighbors for each position
    neighbors = {}
    for r in range(n):
        for c in range(n):
            pos = r * n + c
            neighbors[pos] = []
            if r > 0: neighbors[pos].append((r - 1) * n + c)  # above
            if r < n - 1: neighbors[pos].append((r + 1) * n + c)  # below
            if c > 0: neighbors[pos].append(r * n + (c - 1))  # left
            if c < n - 1: neighbors[pos].append(r * n + (c + 1))  # right

    def is_valid(assignment):
        for pos, val in enumerate(assignment):
            for neighbor in neighbors[pos]:
                if assignment[neighbor] == val:
                    return False
        return True

    # Generating all possible assignments
    total_counts = []

    for pos1 in range(n * n):
        for pos2 in range(n * n):
            count = 0
            # Generate all possible assignments
            for assignment in product(range(q), repeat=n*n):
                if assignment[pos1] == 0 and assignment[pos2] == 0 and is_valid(assignment):
                    count += 1
            total_counts.append(count)

    return total_counts

# Example usage
result = count_valid_assignments(2, 2)
print(result)  # Expected output: [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
