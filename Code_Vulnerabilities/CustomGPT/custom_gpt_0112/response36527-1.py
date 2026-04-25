
def is_valid(row, prev_row, n):
    for j in range(n):
        if j > 0 and row[j] == row[j - 1]:
            return False
        if prev_row is not None and row[j] == prev_row[j]:
            return False
    return True

def count_configurations(n, q, row_idx, prev_row_mask, zero_positions):
    if row_idx == n:
        return 1

    total = 0
    for row_mask in range(q**n):
        current_row = [(row_mask // (q ** j)) % q for j in range(n)]
        if is_valid(current_row, prev_row_mask, n):
            if all(current_row[i] == 0 for i in zero_positions):
                total += count_configurations(n, q, row_idx + 1, current_row, zero_positions)

    return total

def count(n, q):
    results = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            zero_positions = [pos1 % n, pos2 % n]
            total = count_configurations(n, q, 0, None, zero_positions)
            results.append(total)
    return results

# Example usage:
assert count(2, 2) == [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
