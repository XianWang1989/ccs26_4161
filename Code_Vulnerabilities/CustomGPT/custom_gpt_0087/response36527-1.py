
def is_valid(new_row, previous_row, n):
    for j in range(n):
        if (j > 0 and new_row[j] == new_row[j-1]) or (previous_row[j] == new_row[j]):
            return False
    return True

def count_configurations(n, q):
    dp = [[0] * (1 << n) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: 1 way to fill 0 rows

    for i in range(1, n + 1):
        for mask in range(1 << n):
            for new_row in range(q ** n):
                # Convert new_row to a bitmask
                new_mask = 0
                valid = True
                for j in range(n):
                    value = (new_row // (q ** j)) % q
                    if value == 0:
                        new_mask |= (1 << j)

                    if (mask & (1 << j)) and value == 0:
                        valid = False  # Conflict with previous row
                    if j > 0 and value == (new_row // (q ** (j - 1)) % q):
                        valid = False

                if valid and is_valid(new_mask, mask, n):
                    dp[i][new_mask] += dp[i-1][mask]

    total = sum(dp[n][mask] for mask in range(1 << n))
    return total

def count(n, q):
    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            if pos1 == pos2:
                result.append(0)  # Same position, skip
                continue

            total = 0
            for value1 in range(q):
                for value2 in range(q):
                    if value1 != value2:  # Ensure different values
                        total += count_configurations(n, q)
            result.append(total)

    return result

# Example usage
print(count(2, 2))  # Example output for test case
