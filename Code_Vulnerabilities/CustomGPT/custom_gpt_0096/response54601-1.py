
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the marker
    marker_index = next((i for i, line in enumerate(lines) if marker in line), None)

    # Count lines after the marker if found
    if marker_index is not None:
        return len(lines) - marker_index - 1
    else:
        return 0  # Return 0 if marker is not found

# Usage example
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after {marker}: {line_count}")
