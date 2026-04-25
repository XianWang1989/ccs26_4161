
def count_patterns(n, q):
    # Memoization table: dp[mask][row] will store the number of ways to fill 
    # the grid for the given row and color constraints represented by 'mask'.
    dp = {}

    def dfs(row, prev_mask):
        if row == n:
            return 1  # Successfully filled the grid

        if (prev_mask, row) in dp:
            return dp[(prev_mask, row)]

        total_ways = 0
        # Iterate possible current row configurations using bitmask
        for mask in range(1 << (n * 2)):  # 2*n since max two values for each cell
            if is_valid(mask, prev_mask, n, q):
                total_ways += dfs(row + 1, mask)

        dp[(prev_mask, row)] = total_ways
        return total_ways

    def is_valid(current_mask, prev_mask, n, q):
        # Convert mask to color assignment
        current_assignment = [(current_mask >> (i * 2)) & 3 for i in range(n)]

        # Check adjacent cells in current row and previous row
        for i in range(n):
            if current_assignment[i] == current_assignment[i - 1] if i > 0 else -1:
                return False
            if row > 0 and current_assignment[i] == ((prev_mask >> (i * 2)) & 3):
                return False
        return True

    result = []

    for i in range(n**2):
        for j in range(i+1, n**2):  # Ensure (i, j) are distinct positions
            total_patterns = dfs(0, 0)  # Start filling from row 0 with no previous row
            result.append(total_patterns)

    return result

# Example Usage
print(count_patterns(2, 2))  # Replace this with the required n and q
