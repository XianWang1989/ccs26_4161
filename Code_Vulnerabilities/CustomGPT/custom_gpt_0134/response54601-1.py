
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the line containing the marker
    marker_index = None
    for i, line in enumerate(lines):
        if marker in line:
            marker_index = i
            break

    # If marker is found, count lines after it
    if marker_index is not None:
        return len(lines) - (marker_index + 1)
    else:
        return 0  # if the marker isn't found

# Example usage
file_name = "test.ghx"
marker = "{A   B}"
lines_after = count_lines_after_marker(file_name, marker)
print(lines_after)
