
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list

    # Find the index of the line containing the marker
    for i, line in enumerate(lines):
        if marker in line:
            return len(lines) - (i + 1)  # Count remaining lines after the marker

    return 0  # Return 0 if the marker is not found

# Use the function
line_count = count_lines_after_marker("test.ghx", "{A   B}")
print(line_count)
