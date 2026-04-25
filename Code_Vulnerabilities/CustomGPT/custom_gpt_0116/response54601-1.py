
def count_lines_after(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the line containing the marker
    marker_index = next((i for i, line in enumerate(lines) if marker in line), None)

    # If the marker is found, count the lines after it
    if marker_index is not None:
        return len(lines) - marker_index - 1  # Subtract 1 to not count the marker line itself
    else:
        return 0  # Return 0 if the marker is not found

# Example usage
filename = "test.ghx"
marker = "{A   B}"
line_count = count_lines_after(filename, marker)
print(line_count)
