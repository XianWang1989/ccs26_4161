
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the marker line
    try:
        marker_index = lines.index(marker + "\n")  # Add "\n" to match the line correctly
    except ValueError:
        return 0  # Marker not found

    # Count lines after the marker
    return len(lines) - (marker_index + 1)

# Example usage
filename = "test.ghx"
marker = "{A   B}"
line_count = count_lines_after_marker(filename, marker)
print(line_count)
