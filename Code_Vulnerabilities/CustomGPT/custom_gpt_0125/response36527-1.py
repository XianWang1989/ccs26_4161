
def tuples(n, q):
    return [[a] + b for a in range(q) for b in tuples(n-1, q)] if n > 1 else [[a] for a in range(q)]

def is_valid(t, n):
    grid = [t[n*i:n*(i+1)] for i in range(n)]
    for r in range(n):
        for c in range(n):
            v = grid[r][c]
            left = grid[r][c-1] if c > 0 else -1
            right = grid[r][c+1] if c < n - 1 else -1
            top = grid[r-1][c] if r > 0 else -1
            bottom = grid[r+1][c] if r < n - 1 else -1
            if v == left or v == right or v == top or v == bottom:
                return False
    return True

def count(n, q):
    result = []
    for pos1 in range(n**2):
        for pos2 in range(n**2):
            total = sum(1 for t in tuples(n**2, q) if t[pos1] == 0 and t[pos2] == 0 and is_valid(t, n))
            result.append(total)
    return result

assert count(2, 2) == [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
