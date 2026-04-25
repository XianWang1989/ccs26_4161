
def count(n, q):
    from functools import lru_cache

    def valid(mask, n):
        for i in range(n):
            for j in range(n):
                if (mask & (1 << (i * n + j))) == 0:
                    continue
                # Check neighbors
                if i > 0 and (mask & (1 << ((i - 1) * n + j))) != 0:
                    return False
                if j > 0 and (mask & (1 << (i * n + (j - 1)))) != 0:
                    return False
                if i < n - 1 and (mask & (1 << ((i + 1) * n + j))) != 0:
                    return False
                if j < n - 1 and (mask & (1 << (i * n + (j + 1)))) != 0:
                    return False
        return True

    @lru_cache(None)
    def dp(placed, last_row):
        if placed == (1 << (n * n)) - 1:  # All positions filled
            return 1
        total = 0
        for r in range(n):
            for c in range(n):
                pos = r * n + c
                if (placed & (1 << pos)) != 0:
                    continue  # Already placed

                # Check the value we can place here
                for value in range(q):
                    new_mask = placed | (1 << pos)
                    if valid(new_mask, n):
                        total += dp(new_mask, r)

        return total

    result = []
    for i in range(n * n):
        for j in range(n * n):
            if i == j:  # same position
                result.append(0)
                continue
            total = 0
            for t in range(q):
                total += dp(1 << i | 1 << j)  # Mark positions (i, j) as filled
            result.append(total)

    return result

# Example usage
print(count(2, 2))
