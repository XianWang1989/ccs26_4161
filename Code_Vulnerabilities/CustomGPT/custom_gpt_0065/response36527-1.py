
def is_valid(mask, n):
    for r in range(n):
        for c in range(n):
            if (mask & (1 << (r * n + c))) == 0:
                continue
            # Check horizontal neighbors
            if c > 0 and (mask & (1 << (r * n + (c - 1)))) != 0:
                return False
            if c < n - 1 and (mask & (1 << (r * n + (c + 1)))) != 0:
                return False
            # Check vertical neighbors
            if r > 0 and (mask & (1 << ((r - 1) * n + c))) != 0:
                return False
            if r < n - 1 and (mask & (1 << ((r + 1) * n + c))) != 0:
                return False
    return True

def dp(n, q, pos1, pos2, mask, value):
    if pos1 == n * n:
        return 1 if mask != 0 else 0  # valid configuration
    if value >= q:
        return 0

    total = 0
    # Consider current position being filled with 'value'
    if pos1 == (pos2 - 1) or pos1 == (pos2 + 1):
        total += dp(n, q, pos1 + 1, pos2, mask | (1 << pos1), 0)  # using value
    total += dp(n, q, pos1 + 1, pos2, mask, value + 1)  # not using value

    return total

def count(n, q):
    result = []
    for pos1 in range(n * n):
        for pos2 in range(n * n):
            if pos1 == pos2: 
                result.append(0)
                continue
            total = dp(n, q, 0, pos1, 0, 0) + dp(n, q, 0, pos2, 0, 0)
            result.append(total)
    return result

# Test the function
assert count(2, 2) == [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
