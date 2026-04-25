
def is_valid(state, n, row, col, value):
    """Check if placing value at (row, col) is valid."""
    if row > 0 and state[(row - 1) * n + col] == value:
        return False
    if col > 0 and state[row * n + (col - 1)] == value:
        return False
    return True

def count_ways(state, n, q, row, col, positions, memo):
    """Recursive function to count valid configurations."""
    if row == n:  # All rows processed
        return 1

    if col == n:  # Move to next row
        return count_ways(state, n, q, row + 1, 0, positions, memo)

    key = (tuple(state), row, col)
    if key in memo:
        return memo[key]

    total_count = 0
    for value in range(q):
        if is_valid(state, n, row, col, value):
            state[row * n + col] = value  # Set value
            total_count += count_ways(state, n, q, row, col + 1, positions, memo)
            state[row * n + col] = -1  # Reset value (backtrack)

    memo[key] = total_count
    return total_count

def count(n, q):
    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            if pos1 == pos2:
                result.append(0)
                continue

            state = [-1] * (n * n)  # Initialize grid with -1
            state[pos1] = 0  # Set first position
            state[pos2] = 0  # Set second position
            memo = {}
            total = count_ways(state, n, q, 0, 0, [(pos1, pos2)], memo)
            result.append(total)

    return result

# Example usage
print(count(2, 2))
