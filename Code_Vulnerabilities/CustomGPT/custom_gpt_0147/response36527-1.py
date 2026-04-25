
def count(n, q):
    # Memoization table
    dp = [[0] * (1 << (n * n)) for _ in range(n * n)]

    # Initial valid states
    for i in range(1 << (n * n)):
        dp[0][i] = 1  # Base case with a single valid configuration

    for pos in range(1, n * n):
        for state in range(1 << (n * n)):
            for value in range(q):
                # Check if the resulting state is valid
                new_state = state | (value << (pos * 2))
                if is_valid(new_state, n, q):
                    dp[pos][new_state] += dp[pos - 1][state]

    # Count configurations for each (i, j) with value 0
    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 != pos2:
                total = 0
                for state in range(1 << (n * n)):
                    if (state >> (pos1 * 2) & 3) == 0 and (state >> (pos2 * 2) & 3) == 0:  # positions hold `0`
                        total += dp[n * n - 1][state]
                result.append(total)
            else:
                result.append(0)  # Both positions are the same, can't place two zeros

    return result

def is_valid(state, n, q):
    # Check all cells to ensure no two neighbors share the same value
    for r in range(n):
        for c in range(n):
            current_value = (state >> (r * n + c) * 2) & 3
            if current_value == 0:  # Skip if current position is `0`
                continue
            # Check right neighbor
            if c < n - 1 and (current_value == (state >> (r * n + (c + 1)) * 2) & 3):
                return False
            # Check below neighbor
            if r < n - 1 and (current_value == (state >> ((r + 1) * n + c) * 2) & 3):
                return False
    return True

# Example usage
print(count(2, 2))  # Adjust values for n and q as needed
