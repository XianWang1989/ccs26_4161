
def count_lines_after_keyword(filename, keyword):
    with open(filename) as f:
        lines = f.readlines()

    # Find the line number of the keyword
    for index, line in enumerate(lines):
        if keyword in line:
            # Return the count of lines after the keyword
            return len(lines) - index - 1

    # Return 0 if keyword is not found
    return 0

# Example usage
filename = "test.ghx"
keyword = "{A   B}"
line_count = count_lines_after_keyword(filename, keyword)
print(line_count)
