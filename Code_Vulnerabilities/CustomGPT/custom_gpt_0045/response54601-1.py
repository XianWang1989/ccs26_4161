
def count_lines_after_pattern(fname, pattern):
    found_pattern = False
    count = 0

    with open(fname, 'r') as f:
        for line in f:
            if found_pattern:
                count += 1
            if pattern in line:
                found_pattern = True

    return count

# Example usage
lines_after = count_lines_after_pattern("test.ghx", "{A   B}")
print(f"Number of lines after '{{A   B}}': {lines_after}")
