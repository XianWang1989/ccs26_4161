
def is_valid(current_row, previous_row, n):
    for col in range(n):
        if (current_row & (1 << col)) != 0:  # Current color is used in this column
            if previous_row & (1 << col):  # Same color as above
                return False
            if col > 0 and (current_row & (1 << (col - 1))) != 0:  # Same color left
                return False
    return True

def count_valid_assignments(n, q):
    # Precompute valid transitions for every possible row configuration
    valid_transitions = []

    for current in range(1 << n):  # All possible row states
        transitions = []
        for previous in range(1 << n):
            if is_valid(current, previous, n):
                transitions.append(previous)
        valid_transitions.append(transitions)

    dp = [[0] * (1 << n) for _ in range(q)]  # DP table for colors and rows

    # Initialize the DP for the first row
    for r in range(1 << n):
        dp[0][r] = 1

    # Fill DP table for q colors and n rows
    for color in range(1, q):
        for current in range(1 << n):
            for prev in valid_transitions[current]:
                dp[color][current] += dp[color - 1][prev]

    # Count valid configurations avoiding same colors at (i,j) and (k,l)
    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            total = 0
            for row_state in range(1 << n):
                if (row_state & (1 << (pos1 % n))) and (row_state & (1 << (pos2 % n))):
                    total += dp[q - 1][row_state]
            result.append(total)

    return result

# Test with n=2 and q=2
print(count_valid_assignments(2, 2))
