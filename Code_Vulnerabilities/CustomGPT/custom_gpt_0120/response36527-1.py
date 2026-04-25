
def is_valid(mask, prev_mask, q):
    for i in range(len(mask)):
        if (mask[i] & (mask[i] - 1)) >> 1 == prev_mask[i]:  # Check neighbors
            return False
    return True

def count_ways(n, q):
    # dp[mask][row]: Number of ways to fill rows 0 to row with last row as 'mask'
    dp = [[0] * (1 << n) for _ in range(n)]
    dp[0][0] = 1

    for row in range(n):
        for mask in range(1 << n):
            if dp[row][mask] == 0:
                continue
            for next_mask in range(1 << n):
                if is_valid(next_mask, mask, q):
                    dp[row + 1][next_mask] += dp[row][mask]

    return dp[n]

def count(n, q):
    result = []
    for i in range(n * n):
        for j in range(i + 1, n * n):
            total = 0
            for pos1 in range(q):
                for pos2 in range(q):
                    if pos1 == 0 and pos2 == 0:
                        total += count_ways(n, q)[i][j]
            result.append(total)
    return result

# Example usage
print(count(2, 2))
