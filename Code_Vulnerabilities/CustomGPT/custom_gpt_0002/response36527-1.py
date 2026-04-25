
def is_valid(grid, r, c, n):
    return (r == 0 or grid[r-1][c] != grid[r][c]) and (c == 0 or grid[r][c-1] != grid[r][c])

def count_ways(n, q):
    result = []

    def backtrack(grid, zeros):
        if len(zeros) == 2:  # If we have placed '0' in two positions
            if all(is_valid(grid, r, c, n) for r, c in zeros):
                total_count.append(sum(1 for row in grid for val in row if val == 0))
            return

        for r in range(n):
            for c in range(n):
                if (r, c) not in zeros:
                    grid[r][c] = 0
                    zeros.append((r, c))
                    backtrack(grid, zeros)
                    zeros.pop()
                    grid[r][c] = -1  # Reset the position

    for pos1 in range(n * n):
        total_count = []
        grid = [[-1] * n for _ in range(n)]  # Initialize grid with -1
        backtrack(grid, [])
        result.append(sum(total_count))

    return result

# Example usage
print(count_ways(2, 2))  # Example output 
