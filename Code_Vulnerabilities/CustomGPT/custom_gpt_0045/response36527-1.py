
def count_configurations(n, q, i, j, k, l):
    # Initialize an array to hold dynamic programming results
    dp = [[0] * (1 << n) for _ in range(n)]

    # Initial configuration setup
    for mask in range(1 << n):
        if is_valid(mask, i, j, k, l):
            dp[0][mask] = 1

    # Fill the dp table
    for row in range(1, n):
        for mask in range(1 << n):
            if dp[row - 1][mask] > 0:
                for new_mask in range(1 << n):
                    if can_place(mask, new_mask):
                        dp[row][new_mask] += dp[row - 1][mask]

    # Sum valid configurations
    total_count = 0
    for mask in range(1 << n):
        total_count += dp[n - 1][mask]

    return total_count

def is_valid(mask, i, j, k, l):
    # Check that the color at (i, j) and (k, l) is the specified for '0'
    return ((mask >> i) & 1) == 0 and ((mask >> j) & 1) == 0 and ((mask >> k) & 1) == 0 and ((mask >> l) & 1) == 0

def can_place(prev_mask, new_mask):
    for c in range(n):
        if ((prev_mask >> c) & 1) == ((new_mask >> c) & 1):  # Same color in the same column
            return False
        if (c > 0 and ((new_mask >> c) & 1) == ((new_mask >> (c - 1)) & 1)):  # Adjacency check (horizontally)
            return False
    return True

# Example usage
q = 3  # Number of colors
n = 2  # Grid size
results = []
for pos1 in range(n**2):
    for pos2 in range(n**2):
        total = count_configurations(n, q, pos1, pos2)
        results.append(total)

print("Results:", results)
