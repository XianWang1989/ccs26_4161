
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the marker
    for index, line in enumerate(lines):
        if marker in line:
            # Return the count of lines after the marker
            return len(lines) - index - 1

    # Return 0 if the marker is not found
    return 0

# Usage
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print(line_count)
