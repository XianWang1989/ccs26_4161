
def is_valid(mask, prev_mask, n):
    for i in range(n):
        # Check adjacent cells in the current row
        if (mask & (1 << i)) != 0:
            if i > 0 and (mask & (1 << (i - 1))) != 0:  # Check left
                return False
            if i < n - 1 and (mask & (1 << (i + 1))) != 0:  # Check right
                return False
    # Check vertical adjacency with the previous row
    for i in range(n):
        if (mask & (1 << i)) != 0 and (prev_mask & (1 << i)) != 0:
            return False
    return True

def count_configurations(n, q):
    valid_masks = []
    for mask in range(q ** n):
        if is_valid(mask, 0, n):  # Check valid for initial row
            valid_masks.append(mask)

    results = [[0] * (n * n) for _ in range(len(valid_masks))]

    for i in range(n * n):
        for j in range(len(valid_masks)):
            for prev_mask in valid_masks:
                if is_valid(valid_masks[j], prev_mask, n):
                    results[j][i] += 1

    return results

def count(n, q):
    result = count_configurations(n, q)
    total_counts = []
    for pos1 in range(n ** 2):
        for pos2 in range(n ** 2):
            count = 0
            for mask in result:
                if (mask[pos1] == 0) and (mask[pos2] == 0):
                    count += 1
            total_counts.append(count)
    return total_counts

# Example Usage
print(count(2, 2))  # Output should be matched to the expected results
