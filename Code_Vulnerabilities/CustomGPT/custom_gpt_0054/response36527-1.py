
def is_valid(mask1, mask2, q):
    # Check if two rows (represented as masks) are valid
    for col in range(q):
        if (mask1 & (1 << col)) and (mask2 & (1 << col)):
            return False
    return True

def count_valid_configurations(n, q):
    # Memoization cache
    cache = {}

    def dp(row, mask):
        if row == n:
            return 1  # Successfully filled all rows

        if (row, mask) in cache:
            return cache[(row, mask)]

        total = 0
        for next_mask in range(1 << q):  # Generate next row configurations
            if is_valid(mask, next_mask, q):
                total += dp(row + 1, next_mask)

        cache[(row, mask)] = total
        return total

    total_count = 0
    for first_mask in range(1 << q):
        total_count += dp(1, first_mask)  # Start from the second row

    return total_count

# Function to count configurations given positions of zeros
def count(n, q):
    results = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            if pos1 == pos2:
                results.append(0)
                continue
            total = count_valid_configurations(n, q)
            results.append(total)

    return results

# Test case
print(count(2, 2))  # Example output for the grid size 2x2 and q=2
