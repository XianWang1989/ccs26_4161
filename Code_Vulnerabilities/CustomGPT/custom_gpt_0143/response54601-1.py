
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the marker
    marker_index = None
    for i, line in enumerate(lines):
        if marker in line:
            marker_index = i
            break

    # If the marker is found, count lines after it
    if marker_index is not None:
        return len(lines) - marker_index - 1
    else:
        return 0  # Marker not found

# Example usage
count = count_lines_after_marker("test.ghx", "{A   B}")
print(count)
