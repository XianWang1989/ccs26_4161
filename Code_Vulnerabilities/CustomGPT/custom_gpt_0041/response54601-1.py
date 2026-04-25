
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the line with the marker
    for index, line in enumerate(lines):
        if marker in line:
            # Count the lines after the marker
            return len(lines) - index - 1  # Subtract 1 for the marker line

    return 0  # Return 0 if marker is not found

# Example usage
marker = '{A   B}'
lines_count = count_lines_after_marker("test.ghx", marker)
print("Number of lines after marker:", lines_count)
