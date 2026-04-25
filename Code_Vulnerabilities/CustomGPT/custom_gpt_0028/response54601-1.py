
def count_lines_after_keyword(fname, keyword):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the line containing the keyword
    for index, line in enumerate(lines):
        if keyword in line:
            return len(lines) - index - 1  # Count lines after the keyword line

    return 0  # Return 0 if the keyword is not found

# Example usage
line_count = count_lines_after_keyword("test.ghx", "{A   B}")
print(line_count)
