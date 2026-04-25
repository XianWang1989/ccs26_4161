
def dfs(row, grid, n, q, memo):
    if row == n:
        return 1  # Successfully filled all rows
    if (row, grid) in memo:
        return memo[(row, grid)]

    total = 0
    for new_row in range(q**n):
        if is_valid(new_row, grid, n, q):
            total += dfs(row + 1, new_row, n, q, memo)

    memo[(row, grid)] = total
    return total

def is_valid(new_row, prev_row, n, q):
    for col in range(n):
        new_val = (new_row // (q ** col)) % q
        prev_val = (prev_row // (q ** col)) % q
        if new_val == prev_val:
            return False

        if col > 0:
            left_val = (new_row // (q ** (col - 1))) % q
            if new_val == left_val:
                return False

    return True

def count(n, q):
    memo = {}
    result = []

    for pos1 in range(n**2):
        for pos2 in range(n**2):
            if pos1 == pos2:
                result.append(0)  # Same position can't have two zeros
                continue

            total_count = dfs(0, 0, n, q, memo)  # Start from row 0 and empty grid
            result.append(total_count)

    return result

# Example usage
print(count(2, 2))  # Output the counts for the grid of size 2 and q = 2
