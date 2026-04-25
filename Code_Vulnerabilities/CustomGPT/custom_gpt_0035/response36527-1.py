
def is_valid(mask, prev_mask, n, q):
    for col in range(n):
        if ((mask >> col) & (mask >> (col + 1))) or ((prev_mask >> col) & (mask >> col)):
            return False
    return True

def count_ways(n, q):
    dp = {}

    def count(row, prev_mask):
        if row == n:
            return 1  # All rows filled successfully
        if (row, prev_mask) in dp:
            return dp[(row, prev_mask)]

        total = 0
        for mask in range(q ** n):
            if is_valid(mask, prev_mask, n, q):
                total += count(row + 1, mask)

        dp[(row, prev_mask)] = total
        return total

    return count(0, 0)

def count(n, q):
    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            if pos1 == pos2:
                result.append(0)  # Same position not valid
                continue
            total = count_ways(n, q)
            result.append(total)

    return result

# Example usage
print(count(2, 2))  # Adjust for specific parameters as needed
