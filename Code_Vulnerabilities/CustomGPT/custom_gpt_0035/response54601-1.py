
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the line number of the marker
    for index, line in enumerate(lines):
        if marker in line:
            return len(lines) - index - 1  # Count lines after the marker

    return 0  # Return 0 if marker is not found

# Usage
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker}': {line_count}")
