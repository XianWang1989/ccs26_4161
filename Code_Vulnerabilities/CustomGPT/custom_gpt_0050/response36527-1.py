
def is_valid(current_row, previous_row, n):
    for i in range(n):
        if current_row[i] == previous_row[i]:
            return False
        if i > 0 and current_row[i] == current_row[i - 1]:
            return False
    return True

def count_valid_assignments(n, q):
    # Prepare a DP table
    dp = [[[0] * (q) for _ in range(q)] for _ in range(n)]

    # Initialize base cases
    for first in range(q):
        for second in range(q):
            if first != second:
                dp[1][first][second] = 1

    # Fill the DP table
    for row in range(2, n + 1):
        for first in range(q):
            for second in range(q):
                if first != second:
                    for third in range(q):
                        if is_valid((first, second, third), (second, third, first), n):
                            dp[row][first][second] += dp[row - 1][second][third]

    return dp[n]

def total_ways(n, q):
    result = []
    # Iterate through all valid (i,j,k,l) positions
    for i in range(n**2):
        for j in range(i+1, n**2):
            total = 0
            # Count the valid configurations
            for first in range(q):
                for second in range(q):
                    if first == second:
                        continue
                    total += count_valid_assignments(n, q)[first][second]
            result.append(total)

    return result

# Example usage
print(total_ways(2, 2))  # Adjust parameters as needed
