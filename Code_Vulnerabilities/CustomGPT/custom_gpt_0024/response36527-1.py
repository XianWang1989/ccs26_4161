
def is_valid(assignment, n, row, col, value):
    # Check adjacent cells in the grid for conflicts
    if row > 0 and assignment[(row-1) * n + col] == value:  # Above
        return False
    if col > 0 and assignment[row * n + (col-1)] == value:  # Left
        return False
    if row < n-1 and assignment[(row+1) * n + col] == value:  # Below
        return False
    if col < n-1 and assignment[row * n + (col+1)] == value:  # Right
        return False
    return True

def count_colorings(n, q, assignment, positions, index, memo):
    if index == len(positions):
        return 1  # Found a valid way

    pos = positions[index]
    total_ways = 0

    for value in range(q):
        if is_valid(assignment, n, pos[0], pos[1], value):
            assignment[pos[0] * n + pos[1]] = value
            total_ways += count_colorings(n, q, assignment, positions, index + 1, memo)
            assignment[pos[0] * n + pos[1]] = -1  # Reset

    return total_ways

def count(n, q):
    result = []
    for pos1 in range(n*n):
        for pos2 in range(n*n):
            if pos1 != pos2:
                assignment = [-1] * (n * n)
                positions = [(pos1 // n, pos1 % n), (pos2 // n, pos2 % n)]
                assignment[pos1] = 0  # Set first position to 0
                assignment[pos2] = 0  # Set second position to 0
                total = count_colorings(n, q, assignment, positions, 0, {})
                result.append(total)
            else:
                result.append(0)  # Same positions don't count

    return result

# Test the function with an example
assert count(2, 2) == [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
