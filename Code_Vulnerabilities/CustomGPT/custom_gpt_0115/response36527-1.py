
def is_valid(state1, state2, q):
    for i in range(len(state1)):
        if state1[i] == state2[i] or (i > 0 and state1[i] == state1[i - 1]):
            return False
    return True

def count(n, q):
    max_state = (1 << q) - 1
    dp = [[0] * (1 << n) for _ in range(n + 1)]
    result = []

    # Pre-calculate valid states
    valid_states = []
    for state in range(1 << n):
        if len(set((state >> i) & (q - 1) for i in range(n))) != n:
            continue
        valid_states.append(state)

    for pos1 in range(n * n):
        for pos2 in range(n * n):
            total = 0
            for state in valid_states:
                if (state >> (pos1 % n)) & 1 == 0 and (state >> (pos2 % n)) & 1 == 0:
                    dp[0][state] = 1

            for row in range(1, n + 1):
                for prev_state in valid_states:
                    if dp[row - 1][prev_state]:
                        for curr_state in valid_states:
                            if is_valid(prev_state, curr_state, q):
                                dp[row][curr_state] += dp[row - 1][prev_state]

            total += sum(dp[n])

            result.append(total)
            dp = [[0] * (1 << n) for _ in range(n + 1)]  # Reset for next iteration

    return result

# Example Usage
print(count(2, 2))  # Test case
