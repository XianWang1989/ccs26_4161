
def count_valid_grid(n, q):
    # DP array to store the count of valid configurations
    dp = [[0] * (1 << n) for _ in range(n)]

    # Initialize the first row
    for mask in range(1 << n):
        if is_valid_mask(mask, n, q):
            dp[0][mask] = 1

    # Fill the DP table
    for row in range(1, n):
        for curr_mask in range(1 << n):
            if not is_valid_mask(curr_mask, n, q):
                continue
            for prev_mask in range(1 << n):
                if not is_valid_mask(prev_mask, n, q):
                    continue
                if can_place(row, curr_mask, prev_mask):
                    dp[row][curr_mask] += dp[row - 1][prev_mask]

    return dp[n - 1]


def is_valid_mask(mask, n, q):
    # Check if a mask has no two consecutive bits set (adjacent same values).
    for i in range(n - 1):
        if (mask & (1 << i)) == (mask & (1 << (i + 1))):
            return False
    return True


def can_place(row, curr_mask, prev_mask):
    # Check if the current mask can be placed over the previous row's mask
    for i in range(len(curr_mask)):
        if (curr_mask & (1 << i)) == (prev_mask & (1 << i)):
            return False
    return True


def count(n, q):
    results = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2:
                results.append(0)
                continue

            total = 0
            # Count configurations with zeros at pos1 and pos2
            for mask in range(q):
                total += count_valid_grid(n, mask)

            results.append(total)

    return results


# Example usage
print(count(2, 2))
