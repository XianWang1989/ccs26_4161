
def count_lines_after_keyword(fname, keyword):
    with open(fname, 'r') as f:
        lines = f.readlines()

    # Find the index of the line containing the specific keyword
    for index, line in enumerate(lines):
        if keyword in line:
            return len(lines) - index - 1  # Count lines after the keyword

    return 0  # Return 0 if the keyword is not found

# Usage
filename = "test.ghx"
keyword = "{A   B}"
line_count = count_lines_after_keyword(filename, keyword)

print(f"Number of lines after '{keyword}': {line_count}")
