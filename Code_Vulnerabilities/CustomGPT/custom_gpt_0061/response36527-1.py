
def count(n, q):
    from itertools import product

    # Precompute valid states for one row
    valid_states = []
    for state in range(q**n):
        grid_row = [int(x) for x in f"{state:0{n}b}".zfill(n)]
        if all(grid_row[i] != grid_row[i + 1] for i in range(n - 1)):
            valid_states.append(grid_row)

    dp = [[[0] * (q**n) for _ in range(len(valid_states))] for _ in range(n+1)]
    dp[0][0] = 1  # Base case: 1 way to have empty config

    for row in range(1, n + 1):
        for v in range(len(valid_states)):
            for u in range(len(valid_states)):
                # Check if the current state (valid_states[v]) and previous state (valid_states[u]) are valid
                if all(valid_states[v][i] != valid_states[u][i] for i in range(n)):
                    dp[row][v] = (dp[row][v] + dp[row - 1][u]) % (10**9 + 7)

    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            total = 0
            for v in range(len(valid_states)):
                # Check if 0 is placed at pos1 and pos2 in current valid state
                if valid_states[v][pos1 // n] == 0 and valid_states[v][pos2 // n] == 0:
                    total = (total + dp[n][v]) % (10**9 + 7)
            result.append(total)

    return result

# Test case
print(count(2, 2))
