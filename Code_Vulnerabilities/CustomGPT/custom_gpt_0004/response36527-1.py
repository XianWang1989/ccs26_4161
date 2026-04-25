
def count_ways(n, q):
    # Initialize the result array
    result = [[0] * (n * n) for _ in range(n * n)]

    # Generate a valid configuration mask for each cell
    def valid_config(mask):
        # Ensure no two neighbors have the same value
        for i in range(n):
            for j in range(n):
                if (mask & (1 << (i * n + j))) != 0:
                    if j > 0 and (mask & (1 << (i * n + (j - 1)))) != 0:
                        return False
                    if i > 0 and (mask & (1 << ((i - 1) * n + j))) != 0:
                        return False
        return True

    # Iterate over all possible configurations
    for mask in range(1 << (n * n)):
        if valid_config(mask):
            count = [0] * q
            # Count occurrences of each number in this mask
            for num in range(q):
                if (mask & (1 << num)) != 0:
                    count[num] += 1

            # Accumulate the results for every (i,j,k,l)
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        for l in range(n):
                            if i == k and j == l:
                                continue  # Skip if (i,j) == (k,l)
                            result[i * n + j][k * n + l] += 1

    return result

# Example usage
print(count_ways(2, 2))
