
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the line containing the marker
    for i, line in enumerate(lines):
        if marker in line:
            # Return the count of lines after this index
            return len(lines) - (i + 1)

    # If marker not found, return 0
    return 0

# Usage example
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print(line_count)
