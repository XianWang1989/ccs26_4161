
def is_valid(new_row, last_row, n):
    for j in range(n):
        if j > 0 and (new_row & (1 << (last_row[j - 1]))):
            return False
        if last_row[j] == new_row:
            return False
    return True

def count_assignments(n, q):
    dp = [[0] * (1 << q) for _ in range(n + 1)]
    dp[0][0] = 1  # base case: 1 way to fill a 0x0 grid

    for i in range(1, n + 1):
        for row in range(1 << q):
            if dp[i - 1][row] > 0:  # if there's a valid previous row
                for new_row in range(q):
                    if not (row & (1 << new_row)):  # new_row must be different
                        new_mask = row | (1 << new_row)
                        dp[i][new_mask] += dp[i - 1][row]

    result = []
    for pos1 in range(n ** 2):
        for pos2 in range(n ** 2):
            total = 0
            for last_row in range(1 << q):
                if dp[n][last_row] > 0 and (last_row & pos1) == 0 and (last_row & pos2) == 0:
                    total += dp[n][last_row]
            result.append(total)

    return result

# Example usage
n = 2
q = 2
print(count_assignments(n, q))  # Expected output for the example case
