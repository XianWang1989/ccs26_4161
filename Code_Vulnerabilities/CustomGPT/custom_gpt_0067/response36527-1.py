
def is_valid(state, n):
    for r in range(n):
        for c in range(n):
            v = state[r][c]
            if (c > 0 and state[r][c - 1] == v) or (r > 0 and state[r - 1][c] == v):
                return False
    return True

def dp_count(n, q, fixed_positions):
    full_mask = (1 << (n * n)) - 1
    dp = [[0] * (1 << (n * n)) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case

    for mask in range(1 << (n * n)):
        for r in range(n):
            for c in range(n):
                idx = r * n + c
                if (mask & (1 << idx)) == 0:  # If the cell is not yet set
                    for val in range(q):
                        new_mask = mask | (1 << idx)
                        if not (new_mask & (1 << fixed_positions[0]) or new_mask & (1 << fixed_positions[1])):
                            # Set the current cell to `val`
                            if is_valid([[val if (new_mask & (1 << (i * n + j))) else -1 for j in range(n)] for i in range(n)], n):
                                dp[r + (c == n - 1)][new_mask] += dp[r][mask]

    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 != pos2:
                total = sum(dp[n][mask] for mask in range(1 << (n * n)) if (mask & (1 << pos1)) and (mask & (1 << pos2)))
                result.append(total)

    return result

def count(n, q):
    fixed_positions = [0, 1]  # Example fixed positions (0,0) and (0,1)
    return dp_count(n, q, fixed_positions)

# Example usage
print(count(2, 2))  # Should output an array of evaluations for the grid
