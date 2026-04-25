
def count_ways(n, q):
    def valid(prev, curr):
        for j in range(n):
            if j > 0 and curr[j] == prev[j]: return False
            if j < n - 1 and curr[j] == prev[j + 1]: return False
        return True

    dp = [[0] * (q**n) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for num in range(q**n):
            curr = []
            base = 1
            rem = num
            for j in range(n):
                curr.append(rem % q)
                rem //= q
            for prev in range(q**n):
                if dp[i - 1][prev] > 0 and valid([prev // (q**j) % q for j in range(n)], curr):
                    dp[i][num] += dp[i - 1][prev]

    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            total = sum(dp[n][num] for num in range(q**n) if (num >> (n * pos1) & 1 == 0) and (num >> (n * pos2) & 1 == 0))
            result.append(total)

    return result

assert count_ways(2, 2) == [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
