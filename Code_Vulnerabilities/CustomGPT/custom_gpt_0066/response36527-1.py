
def count_valid_colorings(n, q):
    dp = {}

    def dp_helper(row, mask, prev_row):
        if row == n:
            return 1
        if (row, mask, prev_row) in dp:
            return dp[(row, mask, prev_row)]

        total = 0
        for new_mask in range(q ** n):
            if is_valid(new_mask, mask, prev_row, n):
                total += dp_helper(row + 1, new_mask, mask)

        dp[(row, mask, prev_row)] = total
        return total

    def is_valid(new_mask, mask, prev_row, n):
        for j in range(n):
            if j > 0 and (new_mask // (q ** j)) % q == (new_mask // (q ** (j - 1))) % q:
                return False
            if prev_row >= 0 and (new_mask // (q ** j)) % q == (prev_row // (q ** j)) % q:
                return False
        return True

    results = []

    for pos1 in range(n**2):
        for pos2 in range(pos1 + 1, n**2):
            count = dp_helper(0, 0, -1)
            results.append(count)

    return results

# Example usage
result = count_valid_colorings(2, 2)
print(result)  # Output the results
