
def count_lines_after_specific_line(fname, specific_line):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the specific line
    for i, line in enumerate(lines):
        if line.strip() == specific_line:
            return len(lines) - (i + 1)  # Count lines after the specific line

    return 0  # Return 0 if the specific line was not found

# Usage
file_name = "test.ghx"
specific_line = "{A   B}"
line_count = count_lines_after_specific_line(file_name, specific_line)
print(line_count)
