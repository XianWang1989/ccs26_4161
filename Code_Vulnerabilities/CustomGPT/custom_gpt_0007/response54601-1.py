
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the marker line
    marker_index = None
    for i, line in enumerate(lines):
        if marker in line:
            marker_index = i
            break

    # If marker is found, count the lines after it
    if marker_index is not None:
        count_after_marker = len(lines) - marker_index - 1
        return count_after_marker
    else:
        return 0  # Return 0 if marker is not found

# Usage
filename = "test.ghx"
marker = "{A   B}"
count = count_lines_after_marker(filename, marker)
print(count)
