
def count_lines_after_specific_line(fname, search_string):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the specific line
    for index, line in enumerate(lines):
        if search_string in line:
            # Return the count of lines after the found index
            return len(lines) - index - 1

    # If the line is not found, return 0
    return 0

# Usage
file_name = "test.ghx"
specific_line = "{A   B}"
lines_count = count_lines_after_specific_line(file_name, specific_line)
print(lines_count)
